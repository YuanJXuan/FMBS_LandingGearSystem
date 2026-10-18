# ======================================================================
# 路面与轮胎载荷分析系统 - 完整版 (无 pandas 依赖，标签页2支持独立弹窗与导出)
# ======================================================================
import sys
import math
import csv
import os
import numpy as np
from dataclasses import dataclass
from scipy import signal

# PySide2 引入
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *
from PySide2.QtGui import *

# Matplotlib 引入
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

# 解决 matplotlib 显示中文乱码的问题
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False

# ======================================================================
# 第一部分：轮胎算法核心 (用于 标签页1)
# ======================================================================
@dataclass
class AircraftData:
    p_Cx1: float = 1.7204; p_Dx1: float = 0.77751; p_Dx2: float = -0.24431
    p_Ex1: float = 0.46659; p_Ex2: float = 0.393; p_Kx1: float = 14.848
    p_Kx2: float = -9.8161; p_Kx3: float = 0.15818
    p_Cy1: float = 1.5874; p_Dy1: float = 15.0; p_Dy2: float = -0.075004
    p_Ey1: float = 0.37562; p_Ey2: float = -0.069325; p_Ky1: float = -350.0
    p_Ky2: float = 3.3343; p_Ky4: float = 1.0
    r_Bx1: float = 11.13; r_Bx2: float = -12.494; r_Cx1: float = 0.97505
    r_Ex1: float = -0.37196; r_Ex2: float = 0.0017379
    r_By1: float = 13.271; r_By2: float = 5.2405; r_Cy1: float = 1.01
    r_Ey1: float = 0.010513; r_Ey2: float = 5.9816e-5; r_Hy1: float = 0.028005
    r_Hy2: float = -4.8794e-5
    
    F_z0: float = 35000.0; R_tire: float = 0.548; K_z: float = 1e6
    C_z: float = 500.0; m_tire: float = 80.0; g: float = 9.81

_global_aircraft_data = AircraftData()
_z_comp_prev = None; _v_comp_prev = None; _first_call = True

def reset_tire_state():
    global _z_comp_prev, _v_comp_prev, _first_call
    _z_comp_prev = None; _v_comp_prev = None; _first_call = True

def computeTireForces(data, F_z, slip, beta, F_z0):
    dfz = F_z / F_z0 - 1.0
    K_x = slip; C_x = data.p_Cx1
    D_x = F_z * (data.p_Dx1 + data.p_Dx2 * dfz)
    E_x = data.p_Ex1 + data.p_Ex2 * dfz
    B_x = (F_z * (data.p_Kx1 + data.p_Kx2 * dfz) * math.exp(data.p_Kx3 * dfz) / (C_x * D_x + 1e-10))
    BxKx = B_x * K_x
    F_x0 = D_x * math.sin(C_x * math.atan(BxKx - E_x * (BxKx - math.atan(BxKx))))

    beta_y = beta; C_y = data.p_Cy1
    D_y = F_z * (data.p_Dy1 + data.p_Dy2 * dfz)
    E_y = data.p_Ey1 + data.p_Ey2 * dfz
    B_y = (data.p_Ky1 * F_z0 * math.sin(data.p_Ky4 * math.atan((F_z / F_z0) / data.p_Ky2)) / (C_y * D_y + 1e-10))
    ByBeta = B_y * beta_y
    F_y0 = D_y * math.sin(C_y * math.atan(ByBeta - E_y * (ByBeta - math.atan(ByBeta))))

    B_xbeta = data.r_Bx1 * math.cos(math.atan(data.r_Bx2 * slip))
    C_xbeta = data.r_Cx1; E_xbeta = data.r_Ex1 + data.r_Ex2 * dfz
    S_Hxbeta = 0.0; beta_S = beta + S_Hxbeta
    x0 = B_xbeta * S_Hxbeta
    G_xbeta0 = math.cos(C_xbeta * math.atan(x0 - E_xbeta * (x0 - math.atan(x0))))
    xb = B_xbeta * beta_S
    G_xbeta = math.cos(C_xbeta * math.atan(xb - E_xbeta * (xb - math.atan(xb)))) / (G_xbeta0 + 1e-10)
    F_x = F_x0 * G_xbeta

    B_yslip = data.r_By1 * math.cos(math.atan(data.r_By2 * beta))
    C_yslip = data.r_Cy1; E_yslip = data.r_Ey1 + data.r_Ey2 * dfz
    S_Hyslip = data.r_Hy1 + data.r_Hy2 * dfz
    slip_S = slip + S_Hyslip
    y0 = B_yslip * S_Hyslip
    G_yslip0 = math.cos(C_yslip * math.atan(y0 - E_yslip * (y0 - math.atan(y0))))
    ys = B_yslip * slip_S
    G_yslip = math.cos(C_yslip * math.atan(ys - E_yslip * (ys - math.atan(ys)))) / (G_yslip0 + 1e-10)
    F_y = F_y0 * G_yslip
    return F_x, F_y, 0.0

def MagicFormula2(omega, V_x, V_y, delta, dt, reset=False, v_init=0.0):
    global _z_comp_prev, _v_comp_prev, _first_call
    data = _global_aircraft_data
    if _first_call or reset:
        z_static = data.m_tire * data.g / data.K_z
        _z_comp_prev = max(0.0, min(z_static, data.R_tire))
        _v_comp_prev = float(v_init)
        _first_call = False

    F_z = data.K_z * _z_comp_prev + data.C_z * _v_comp_prev
    if F_z < 0.0: F_z = 0.0
    R_rolling = max(data.R_tire - (1.0 / 3.0) * _z_comp_prev, 0.05)
    epsV = 0.01

    if abs(V_x) < epsV:
        slip = 0.0; beta = delta
    else:
        slip = (V_x - omega * R_rolling) / max(abs(V_x), epsV)
        beta = delta - math.atan2(V_y, V_x)

    slip = max(-1.0, min(1.0, slip))
    F_x_raw, F_y_raw, _ = computeTireForces(data, F_z, slip, beta, data.F_z0)
    
    a = data.g - F_z / data.m_tire
    v_comp_new = _v_comp_prev + a * dt
    z_comp_new = _z_comp_prev + v_comp_new * dt

    if z_comp_new < 0.0: z_comp_new = 0.0; v_comp_new = 0.0
    elif z_comp_new > data.R_tire: z_comp_new = data.R_tire; v_comp_new = 0.0
    _z_comp_prev = z_comp_new; _v_comp_prev = v_comp_new

    return -F_x_raw, -F_y_raw, 0.0, _z_comp_prev, _v_comp_prev, R_rolling


# ======================================================================
# 第二部分：非国军标路面载荷图谱核心算法 (用于 标签页2)
# ======================================================================
def get_opt(opts, name, default_val):
    if not isinstance(opts, dict) or name not in opts: return default_val
    value = opts[name]
    if value is None: return default_val
    return value

def generate_synthetic_load(fs, opts):
    duration = float(get_opt(opts, "SyntheticDuration", 20))
    m = int(get_opt(opts, "SyntheticNumChannels", 4))
    base_load = float(get_opt(opts, "SyntheticBaseLoad", 1000))
    noise_level = float(get_opt(opts, "SyntheticNoiseLevel", 30))
    impact_count = int(get_opt(opts, "SyntheticImpactCount", 10))
    rng = np.random.RandomState(1)
    
    n = int(round(duration * fs))
    time = np.arange(n, dtype=float) / fs
    data = np.zeros((n, m), dtype=float)

    for ch0 in range(m):
        ch = ch0 + 1
        f1, f2, f3 = 1.0 + 0.4 * ch, 6.0 + 1.2 * ch, 18.0 + 2.5 * ch
        a1 = base_load * (0.08 + 0.015 * ch)
        a2 = base_load * (0.04 + 0.010 * ch)
        a3 = base_load * (0.020 + 0.005 * ch)

        slow = base_load * 0.04 * np.sin(2 * np.pi * 0.08 * time + ch)
        vib = (a1 * np.sin(2 * np.pi * f1 * time + 0.3 * ch) + 
               a2 * np.sin(2 * np.pi * f2 * time + 0.6 * ch) + 
               a3 * np.sin(2 * np.pi * f3 * time + 0.9 * ch))
        noise = noise_level * rng.randn(n)

        impact = np.zeros(n, dtype=float)
        impact_time = np.sort(rng.rand(impact_count) * duration)
        for t0 in impact_time:
            amp = base_load * (0.10 + 0.08 * rng.rand()) * (0.8 + 0.1 * ch)
            width = 0.015 + 0.025 * rng.rand()
            impact += amp * np.exp(-((time - t0) ** 2) / (2 * width**2))

        data[:, ch0] = base_load * (0.8 + 0.18 * ch) + slow + vib + impact + noise

    return data, time

def load_experimental_file(file_path, fs):
    try:
        raw_data = []
        with open(file_path, 'r', encoding='utf-8-sig', errors='ignore') as f:
            for line in f:
                parts = line.replace(',', ' ').split()
                float_row = []
                for p in parts:
                    try:
                        float_row.append(float(p))
                    except ValueError:
                        float_row.append(np.nan) 
                if float_row:
                    raw_data.append(float_row)
                    
        if not raw_data:
            raise ValueError("文件中没有找到有效的数值数据！")

        raw = np.array(raw_data)
        if raw.ndim != 2: raw = np.atleast_2d(raw)
        
        keep_columns = np.any(np.isfinite(raw), axis=0)
        raw = raw[:, keep_columns]
        
        time = raw[:, 0]
        data = raw[:, 1:]
        valid = np.isfinite(time) & np.all(np.isfinite(data), axis=1)
        
        return data[valid, :], time[valid]
    except Exception as exc:
        raise ValueError(f"文件读取失败（请确保文件为数值型CSV或TXT格式）：{exc}")

def filter_signal(x, fs):
    nyq = fs / 2.0
    band = np.array([0.5, 80], dtype=float)
    b, a = signal.butter(4, band / nyq, btype="bandpass")
    return signal.filtfilt(b, a, x)

def fft_reconstruct(x, fs, keep_ratio=0.95):
    n = len(x)
    nfft = 1 << (n - 1).bit_length() if n > 1 else 1
    x_fft = np.fft.fft(x, n=nfft)
    half_n = nfft // 2 + 1
    
    pos_idx = np.arange(half_n)
    energy = np.abs(x_fft[pos_idx]) ** 2
    if len(energy): energy[0] = 0.0 
    
    total_energy = float(np.sum(energy))
    order = np.argsort(energy)[::-1]
    cumulative = np.cumsum(energy[order]) / (total_energy + 1e-12)
    hit = np.flatnonzero(cumulative >= keep_ratio)
    n_keep = int(hit[0] + 1) if len(hit) else len(order)
    
    keep_pos_idx = np.unique(np.concatenate(([0], order[:n_keep]))).astype(int)
    keep_mask = np.zeros(nfft, dtype=bool)
    keep_mask[keep_pos_idx] = True
    for idx in keep_pos_idx:
        if 0 < idx < nfft // 2: keep_mask[nfft - idx] = True
            
    x_recon_fft = np.zeros_like(x_fft)
    x_recon_fft[keep_mask] = x_fft[keep_mask]
    
    tmp = np.real(np.fft.ifft(x_recon_fft, n=nfft))
    xr = tmp[:n]
    
    rms0 = float(np.sqrt(np.mean(x**2)))
    rms1 = float(np.sqrt(np.mean(xr**2)))
    if rms1 > 1e-12: xr = xr * rms0 / rms1
    return xr

def _rainflow_cycles(series):
    x = np.asarray(series, dtype=float).reshape(-1)
    x = x[np.isfinite(x)]
    if len(x) == 0: return {}
    
    compact = [float(x[0])]
    for v in x[1:]:
        if float(v) != compact[-1]: compact.append(float(v))
        
    rev = [compact[0]]
    for i in range(1, len(compact) - 1):
        if (compact[i] - compact[i - 1]) * (compact[i + 1] - compact[i]) <= 0:
            rev.append(compact[i])
    rev.append(compact[-1])
    
    stack, cycles = [], []
    for p in rev:
        stack.append(p)
        while len(stack) >= 3:
            r1, r2 = abs(stack[-2] - stack[-3]), abs(stack[-1] - stack[-2])
            if r2 < r1: break
            mean_val = 0.5 * (stack[-3] + stack[-2])
            if len(stack) == 3:
                cycles.append((0.5, r1, mean_val))
                stack.pop(0)
            else:
                cycles.append((1.0, r1, mean_val))
                last = stack[-1]
                del stack[-3:]
                stack.append(last)
                
    for i in range(len(stack) - 1):
        cycles.append((0.5, abs(stack[i + 1] - stack[i]), 0.5 * (stack[i + 1] + stack[i])))
        
    if not cycles: return {}
    cycles_arr = np.array(cycles)
    return {
        "Count": cycles_arr[:, 0],
        "Range": cycles_arr[:, 1],
        "Mean": cycles_arr[:, 2]
    }

def process_load_spectrum(data, time, fs):
    n, m = data.shape
    pre, dyn, rec = np.zeros((n, m)), np.zeros((n, m)), np.zeros((n, m))
    
    for ch in range(m):
        x = data[:, ch]
        trend = np.full(n, np.nanmean(x))
        xb = x - trend
        xf = filter_signal(xb, fs)
        pre[:, ch] = xf + trend
        dyn[:, ch] = xf
        rec[:, ch] = fft_reconstruct(dyn[:, ch], fs, 0.95)
        rec[:, ch] += trend
        
    result = {
        "time": time,
        "rawLoad": data,
        "preprocessedLoad": pre,
        "reconstructedLoad": rec,
        "fatigue": {"channel": []},
        "frequency": {"channel": []},
    }
    
    for ch in range(m):
        # 频谱
        x = dyn[:, ch]
        nfft = 1 << (len(x) - 1).bit_length() if len(x) > 1 else 1
        x_fft = np.fft.fft(x, n=nfft)
        half_n = nfft // 2 + 1
        f_hz = fs * np.arange(half_n, dtype=float) / nfft
        amp = np.abs(x_fft[:half_n]) / len(x)
        if len(amp) > 2: amp[1:-1] *= 2.0
        result["frequency"]["channel"].append({"fHz": f_hz, "amplitude": amp})
        
        # 雨流
        cycle_table = _rainflow_cycles(rec[:, ch])
        if cycle_table:
            ranges = cycle_table["Range"]
            means = cycle_table["Mean"]
            counts = cycle_table["Count"]
            
            r_edges = np.linspace(ranges.min(), ranges.max(), 17)
            m_edges = np.linspace(means.min(), means.max(), 17)
            count_matrix, _, _ = np.histogram2d(ranges, means, bins=[r_edges, m_edges], weights=counts)
            result["fatigue"]["channel"].append({
                "available": True, "countMatrix": count_matrix, 
                "rangeEdges": r_edges, "meanEdges": m_edges
            })
        else:
            result["fatigue"]["channel"].append({"available": False})
            
    return result

# ======================================================================
# 弹窗类 1 (用于 标签页1: 轮胎接触算法结果)
# ======================================================================
class PlotResultDialog(QDialog):
    def __init__(self, time_plot, V_x_plot, V_y_plot, omega_plot, slip, Fx, Fy, Fz, beta, parent=None):
        super(PlotResultDialog, self).__init__(parent)
        self.setWindowTitle("计算结果 - 魔术公式轮胎模型")
        self.resize(1200, 850)
        
        self.time_plot = time_plot; self.V_x_plot = V_x_plot; self.V_y_plot = V_y_plot
        self.omega_plot = omega_plot; self.slip = slip; self.Fx = Fx
        self.Fy = Fy; self.Fz = Fz; self.beta = beta
        
        layout = QVBoxLayout(self)
        toolbar_layout = QHBoxLayout()
        self.exportButton = QPushButton("导出 8 组图表数据 (CSV)")
        self.exportButton.setMinimumHeight(35)
        self.exportButton.clicked.connect(self.exportToCsvEvent)
        toolbar_layout.addStretch()
        toolbar_layout.addWidget(self.exportButton)
        layout.addLayout(toolbar_layout)

        fig = Figure(figsize=(12, 9), dpi=100)
        fig.suptitle("魔术公式轮胎模型", fontsize=16, fontweight='bold')
        axes = fig.subplots(3, 3)

        axes[0,0].plot(time_plot, V_x_plot, color='blue'); axes[0,0].grid(True); axes[0,0].set_title("纵向速度 V_x")
        axes[0,1].plot(time_plot, V_y_plot, color='red'); axes[0,1].grid(True); axes[0,1].set_title("侧向速度 V_y")
        axes[0,2].plot(time_plot, omega_plot, color='black'); axes[0,2].grid(True); axes[0,2].set_title("轮胎角速度 ω")
        axes[1,0].plot(time_plot, slip, color='lime'); axes[1,0].grid(True); axes[1,0].set_title("滑移率")
        axes[1,1].plot(time_plot, Fx, color='magenta'); axes[1,1].grid(True); axes[1,1].set_title("纵向力 F_x")
        axes[1,2].plot(time_plot, Fy, color='cyan'); axes[1,2].grid(True); axes[1,2].set_title("侧向力 F_y")
        axes[2,0].plot(time_plot, Fz, color='gray'); axes[2,0].grid(True); axes[2,0].set_title("垂向力 F_z")
        axes[2,1].plot(time_plot, beta, color='orchid'); axes[2,1].grid(True); axes[2,1].set_title("侧偏角 β")
        axes[2,2].axis("off")
        fig.tight_layout(rect=[0, 0, 1, 0.96])

        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)

    def exportToCsvEvent(self):
        folder_path = QFileDialog.getExistingDirectory(self, "选择保存数据文件的文件夹")
        if not folder_path: return
        try:
            datasets = {
                "01_纵向速度_Vx.csv": (self.time_plot, self.V_x_plot, "时间 (s)", "纵向速度 (m/s)"),
                "02_侧向速度_Vy.csv": (self.time_plot, self.V_y_plot, "时间 (s)", "侧向速度 (m/s)"),
                "03_轮胎角速度_omega.csv": (self.time_plot, self.omega_plot, "时间 (s)", "角速度 (rad/s)"),
                "04_滑移率_slip.csv": (self.time_plot, self.slip, "时间 (s)", "滑移率"),
                "05_纵向力_Fx.csv": (self.time_plot, self.Fx, "时间 (s)", "纵向力 (N)"),
                "06_侧向力_Fy.csv": (self.time_plot, self.Fy, "时间 (s)", "侧向力 (N)"),
                "07_垂向力_Fz.csv": (self.time_plot, self.Fz, "时间 (s)", "垂向力 (N)"),
                "08_侧偏角_beta.csv": (self.time_plot, self.beta, "时间 (s)", "侧偏角 (rad)")
            }
            for filename, (x_data, y_data, x_col, y_col) in datasets.items():
                full_path = os.path.join(folder_path, filename)
                with open(full_path, mode='w', newline='', encoding='utf-8-sig') as file:
                    writer = csv.writer(file)
                    writer.writerow([x_col, y_col])
                    for x, y in zip(x_data, y_data):
                        writer.writerow([x, y])
            QMessageBox.information(self, "导出成功", "图表数据已成功导出为CSV文件。")
        except Exception as e:
            QMessageBox.critical(self, "导出失败", f"导出过程中发生错误：\n{str(e)}")

# ======================================================================
# 弹窗类 2 (用于 标签页2: 非国军标路面载荷重构)
# ======================================================================
class LoadSpectrumPlotDialog(QDialog):
    def __init__(self, result_dict, parent=None):
        super(LoadSpectrumPlotDialog, self).__init__(parent)
        self.setWindowTitle("计算结果 - 非国军标载荷谱重构")
        self.resize(1100, 800)
        self.result = result_dict
        
        layout = QVBoxLayout(self)
        toolbar_layout = QHBoxLayout()
        self.exportButton = QPushButton("导出图表数据 (CSV)")
        self.exportButton.setMinimumHeight(35)
        self.exportButton.clicked.connect(self.exportToCsvEvent)
        toolbar_layout.addStretch()
        toolbar_layout.addWidget(self.exportButton)
        layout.addLayout(toolbar_layout)

        fig = Figure(figsize=(10, 8), dpi=100)
        fig.subplots_adjust(hspace=0.35, wspace=0.25)
        ax1 = fig.add_subplot(221)
        ax2 = fig.add_subplot(222)
        ax3 = fig.add_subplot(223)
        ax4 = fig.add_subplot(224)

        time = self.result["time"]
        ch0 = 0 
        
        # 1. 载荷谱重构对比
        ax1.plot(time, self.result["rawLoad"][:, ch0], label="原始/合成载荷")
        ax1.plot(time, self.result["preprocessedLoad"][:, ch0], label="预处理后")
        ax1.plot(time, self.result["reconstructedLoad"][:, ch0], label="重构载荷")
        ax1.grid(True); ax1.set_xlabel("时间 (s)"); ax1.set_ylabel("载荷")
        ax1.set_title("关键通道 1 载荷谱重构")
        ax1.legend(fontsize=8)

        # 2. 多通道对比
        if self.result["rawLoad"].shape[1] > 1:
            for k in range(min(self.result["rawLoad"].shape[1], 4)):
                ax2.plot(time, self.result["reconstructedLoad"][:, k], label=f"通道 {k+1}")
        else:
            ax2.plot(time, self.result["reconstructedLoad"][:, 0], label="通道 1")
        ax2.grid(True); ax2.set_xlabel("时间 (s)"); ax2.set_ylabel("重构载荷")
        ax2.set_title("关键位置重构载荷谱对比")
        ax2.legend(fontsize=8)

        # 3. 频谱分析
        f = self.result["frequency"]["channel"][ch0]
        ax3.plot(f["fHz"], f["amplitude"])
        ax3.grid(True); ax3.set_xlabel("频率 (Hz)"); ax3.set_ylabel("幅值")
        ax3.set_title("频谱分析")

        # 4. 雨流计数
        rf = self.result["fatigue"]["channel"][ch0]
        if rf["available"]:
            extent = [rf["meanEdges"][0], rf["meanEdges"][-1], rf["rangeEdges"][0], rf["rangeEdges"][-1]]
            im = ax4.imshow(rf["countMatrix"], origin="lower", aspect="auto", extent=extent, cmap='jet')
            fig.colorbar(im, ax=ax4)
            ax4.set_xlabel("均值载荷"); ax4.set_ylabel("载荷范围")
            ax4.set_title("雨流计数载荷谱")
        else:
            ax4.text(0.5, 0.5, "雨流计数无有效循环", ha='center', va='center')
            ax4.axis('off')

        fig.tight_layout()
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)

    def exportToCsvEvent(self):
        folder_path = QFileDialog.getExistingDirectory(self, "选择保存数据文件的文件夹")
        if not folder_path: return
        try:
            time = self.result["time"]
            
            # 导出通道1时间序列数据
            with open(os.path.join(folder_path, "01_载荷对比_通道1.csv"), 'w', newline='', encoding='utf-8-sig') as f:
                w = csv.writer(f)
                w.writerow(["时间(s)", "原始载荷", "预处理后载荷", "重构载荷"])
                for t, raw, pre, rec in zip(time, self.result["rawLoad"][:,0], self.result["preprocessedLoad"][:,0], self.result["reconstructedLoad"][:,0]):
                    w.writerow([t, raw, pre, rec])
                    
            # 导出多通道重构载荷数据
            with open(os.path.join(folder_path, "02_重构载荷_多通道对比.csv"), 'w', newline='', encoding='utf-8-sig') as f:
                w = csv.writer(f)
                headers = ["时间(s)"] + [f"通道_{i+1}_重构载荷" for i in range(self.result["reconstructedLoad"].shape[1])]
                w.writerow(headers)
                for i in range(len(time)):
                    row = [time[i]] + list(self.result["reconstructedLoad"][i, :])
                    w.writerow(row)
            
            # 导出通道1频谱数据
            f_data = self.result["frequency"]["channel"][0]
            with open(os.path.join(folder_path, "03_频谱分析_通道1.csv"), 'w', newline='', encoding='utf-8-sig') as f:
                w = csv.writer(f)
                w.writerow(["频率(Hz)", "幅值"])
                for hz, amp in zip(f_data["fHz"], f_data["amplitude"]):
                    w.writerow([hz, amp])

            QMessageBox.information(self, "导出成功", "载荷谱数据已成功导出为CSV文件。")
        except Exception as e:
            QMessageBox.critical(self, "导出失败", f"导出发生错误：\n{str(e)}")

# ======================================================================
# 主窗体定义
# ======================================================================
class TireAnalysisDialog(QDialog):
    def __init__(self, parent=None):
        super(TireAnalysisDialog, self).__init__(parent)
        self.initUI()
        self.resize(800, 450)

    def initUI(self):
        self.mainGridLayout = QGridLayout(self)

        self.infoTabWidget = QTabWidget()
        self.mainGridLayout.addWidget(self.infoTabWidget, 0, 0, 1, 1)

        self.tireAlgoSubTabWidget = QWidget()
        self.roadLoadSubTabWidget = QWidget()
        self.modelLibSubTabWidget = QWidget()

        self.infoTabWidget.addTab(self.tireAlgoSubTabWidget, "轮胎地面接触算法")
        self.infoTabWidget.addTab(self.roadLoadSubTabWidget, "非国军标路面载荷图谱")
        self.infoTabWidget.addTab(self.modelLibSubTabWidget, "路面载荷模型库")

        self.setupTireAlgoTab()
        self.setupRoadLoadTab()
        self.setupModelLibTab() 

    # ------------------ 标签页 1：轮胎地面接触算法 ------------------
    def setupTireAlgoTab(self):
        self.tireAlgoLayout = QGridLayout(self.tireAlgoSubTabWidget)
        parameters = [
            ("轮胎静态垂向载荷 F_z0 (N)", "35000.0", "F_z0"),
            ("轮胎名义半径 R_tire (m)", "0.548", "R_tire"),
            ("轮胎垂向刚度 K_z (N/m)", "1000000.0", "K_z"),
            ("轮胎垂向阻尼 C_z (N·s/m)", "500.0", "C_z"),
            ("轮胎等效质量 m_tire (kg)", "80.0", "m_tire"),
            ("重力加速度 g (m/s^2)", "9.81", "g"),
            ("飞机质量 m_aircraft (kg)", "3000.0", "m_aircraft"),
            ("轮胎转动惯量 I_wheel (kg·m^2)", "0.5", "I_wheel"),
            ("初始纵向速度 V_x0 (m/s)", "70.0", "V_x0"),
            ("初始侧向速度 V_y0 (m/s)", "2.0", "V_y0"),
            ("初始轮胎角速度 omega0 (rad/s)", "0.0", "omega0"),
            ("初始压缩速度 v_init (m/s)", "-0.5", "v_init"),
            ("转向角 delta (rad)", "0.0", "delta")
        ]

        self.paramEntries = {}
        for i, (name, default_val, var_key) in enumerate(parameters):
            row, col = i // 2, (i % 2) * 2
            lbl = QLabel(name + "：")
            lbl.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.tireAlgoLayout.addWidget(lbl, row, col)
            ent = QLineEdit(default_val)
            self.tireAlgoLayout.addWidget(ent, row, col + 1)
            self.paramEntries[var_key] = ent

        self.calcButton = QPushButton("运行真实物理仿真模型")
        self.calcButton.clicked.connect(self.calculateClickedEvent)
        self.calcButton.setMinimumHeight(40)
        self.tireAlgoLayout.addWidget(self.calcButton, 7, 0, 1, 4, Qt.AlignCenter)

    def calculateClickedEvent(self):
        try:
            p = {k: float(v.text()) for k, v in self.paramEntries.items()}
            _global_aircraft_data.F_z0 = p["F_z0"]
            _global_aircraft_data.R_tire = p["R_tire"]
            _global_aircraft_data.K_z = p["K_z"]
            _global_aircraft_data.C_z = p["C_z"]
            _global_aircraft_data.m_tire = p["m_tire"]
            _global_aircraft_data.g = p["g"]

            dt, t_end = 0.001, 10.0
            Nsteps = round(t_end / dt)

            time_arr = np.zeros(Nsteps)
            V_x, V_y, omega = np.zeros(Nsteps + 1), np.zeros(Nsteps + 1), np.zeros(Nsteps + 1)
            Fx, Fy, Fz = np.zeros(Nsteps), np.zeros(Nsteps), np.zeros(Nsteps)
            slip, beta = np.zeros(Nsteps), np.zeros(Nsteps)

            V_x[0], V_y[0], omega[0] = p["V_x0"], p["V_y0"], p["omega0"]
            reset_tire_state()
            reset_flag, v_init_val = True, p["v_init"]
            
            for i in range(Nsteps):
                time_arr[i] = i * dt
                if abs(V_x[i]) > 0.01:
                    beta[i] = p["delta"] - np.arctan2(V_y[i], V_x[i])
                else:
                    beta[i] = p["delta"]

                Fx_i, Fy_i, _, z_comp_i, v_comp_i, R_rolling = MagicFormula2(
                    omega[i], V_x[i], V_y[i], p["delta"], dt, reset_flag, v_init_val
                )

                reset_flag = False; v_init_val = 0.0
                Fx[i], Fy[i] = Fx_i, Fy_i
                Fz[i] = _global_aircraft_data.K_z * z_comp_i + _global_aircraft_data.C_z * v_comp_i

                if abs(V_x[i]) > 0.01:
                    slip[i] = (V_x[i] - omega[i] * R_rolling) / abs(V_x[i])
                else:
                    slip[i] = 0.0

                V_x[i + 1] = max(0.0, V_x[i] + (Fx_i / p["m_aircraft"]) * dt)
                V_y[i + 1] = V_y[i] + (Fy_i / p["m_aircraft"]) * dt
                omega[i + 1] = max(0.0, omega[i] + (-Fx_i * R_rolling / p["I_wheel"]) * dt)

            self.plot_dialog = PlotResultDialog(
                time_arr, V_x[:-1], V_y[:-1], omega[:-1], slip, Fx, Fy, Fz, beta, parent=self
            )
            self.plot_dialog.exec_() 

        except ValueError:
            QMessageBox.critical(self, "输入错误", "请确保所有参数输入均为有效的数值！")


    # ------------------ 标签页 2：非国军标路面载荷图谱 ------------------
    def setupRoadLoadTab(self):
        self.roadLoadLayout = QVBoxLayout(self.roadLoadSubTabWidget)

        # 创建一个居中的布局容器
        container = QWidget()
        container_layout = QVBoxLayout(container)
        container.setMaximumWidth(450)

        self.loadModeCombo = QComboBox()
        self.loadModeCombo.addItems(["模式 1 (模拟数据生成)", "模式 2 (实验数据输入)"])
        self.loadModeCombo.currentIndexChanged.connect(self.onLoadModeChanged)
        container_layout.addWidget(QLabel("选择数据模式："))
        container_layout.addWidget(self.loadModeCombo)
        container_layout.addSpacing(10)

        self.fs_input = QLineEdit("1000")
        container_layout.addWidget(QLabel("采样频率 FS (Hz)："))
        container_layout.addWidget(self.fs_input)
        container_layout.addSpacing(10)

        self.loadStackedWidget = QStackedWidget()

        # 模式 1
        page_mode1 = QWidget()
        form_mode1 = QFormLayout(page_mode1)
        self.m1_duration = QLineEdit("20")
        self.m1_channels = QLineEdit("4")
        self.m1_baseload = QLineEdit("1000")
        self.m1_noise = QLineEdit("30")
        form_mode1.addRow("模拟时长 (s):", self.m1_duration)
        form_mode1.addRow("通道数量:", self.m1_channels)
        form_mode1.addRow("基础载荷:", self.m1_baseload)
        form_mode1.addRow("噪声水平:", self.m1_noise)
        self.loadStackedWidget.addWidget(page_mode1)

        # 模式 2
        page_mode2 = QWidget()
        form_mode2 = QVBoxLayout(page_mode2)
        self.m2_filepath = QLineEdit()
        btn_browse = QPushButton("浏览文件 (CSV/TXT)...")
        btn_browse.clicked.connect(self.browseExperimentalFile)
        form_mode2.addWidget(QLabel("实验数据文件:"))
        form_mode2.addWidget(self.m2_filepath)
        form_mode2.addWidget(btn_browse)
        form_mode2.addStretch()
        self.loadStackedWidget.addWidget(page_mode2)

        container_layout.addWidget(self.loadStackedWidget)
        container_layout.addSpacing(20)

        btn_calc_load = QPushButton("计算并绘制载荷图谱")
        btn_calc_load.setMinimumHeight(45)
        btn_calc_load.clicked.connect(self.calcRoadLoadEvent)
        container_layout.addWidget(btn_calc_load)

        # 将容器居中放置
        wrapper_layout = QHBoxLayout()
        wrapper_layout.addStretch()
        wrapper_layout.addWidget(container)
        wrapper_layout.addStretch()
        
        self.roadLoadLayout.addLayout(wrapper_layout)

    def onLoadModeChanged(self, index):
        self.loadStackedWidget.setCurrentIndex(index)

    def browseExperimentalFile(self):
        filepath, _ = QFileDialog.getOpenFileName(self, "选择实验数据文件", "", "数据文件 (*.csv *.txt)")
        if filepath:
            self.m2_filepath.setText(filepath)

    def calcRoadLoadEvent(self):
        try:
            mode = self.loadModeCombo.currentIndex()
            fs = float(self.fs_input.text())
            opts = {}
            
            if mode == 0:
                opts["SyntheticDuration"] = float(self.m1_duration.text())
                opts["SyntheticNumChannels"] = int(self.m1_channels.text())
                opts["SyntheticBaseLoad"] = float(self.m1_baseload.text())
                opts["SyntheticNoiseLevel"] = float(self.m1_noise.text())
                data, time = generate_synthetic_load(fs, opts)
            else:
                filepath = self.m2_filepath.text()
                if not filepath or not os.path.exists(filepath):
                    QMessageBox.warning(self, "文件错误", "请先选择一个有效的实验数据文件！")
                    return
                data, time = load_experimental_file(filepath, fs)

            result = process_load_spectrum(data, time, fs)

            # 调用我们新写的独立弹窗类
            self.load_plot_dialog = LoadSpectrumPlotDialog(result, parent=self)
            self.load_plot_dialog.exec_()
            
        except Exception as e:
            QMessageBox.critical(self, "计算错误", f"计算过程中发生错误：\n{str(e)}")


    # ------------------ 标签页 3：路面载荷模型库 ------------------
    def setupModelLibTab(self):
        self.modelLibLayout = QHBoxLayout(self.modelLibSubTabWidget)

        left_panel = QFrame()
        left_layout = QVBoxLayout(left_panel)
        left_panel.setMinimumWidth(400)
        left_panel.setMaximumWidth(450)

        type_layout = QHBoxLayout()
        type_layout.addWidget(QLabel("选择道面类型："))
        self.roadTypeCombo = QComboBox()
        self.roadTypeCombo.addItems(["简谐道面", "随机道面"])
        self.roadTypeCombo.currentIndexChanged.connect(self.onRoadTypeChanged)
        type_layout.addWidget(self.roadTypeCombo)
        left_layout.addLayout(type_layout)

        self.stackedWidget = QStackedWidget()

        page_harm = QWidget()
        form_harm = QFormLayout(page_harm)
        self.harm_subtype_combo = QComboBox()
        self.harm_subtype_combo.addItems(["铺砌简谐道面", "半铺砌简谐道面", "未铺砌简谐道面"])
        form_harm.addRow("道面子类型:", self.harm_subtype_combo)
        self.harm_xmax_input = QLineEdit("62.83") 
        form_harm.addRow("道面长度 x_max:", self.harm_xmax_input)
        self.harm_n_input = QLineEdit("500")
        form_harm.addRow("采样点数 N:", self.harm_n_input)
        self.harm_L_input = QLineEdit("100.0")
        form_harm.addRow("波长参数 L (仅未铺砌):", self.harm_L_input)
        self.stackedWidget.addWidget(page_harm)

        page_rand = QWidget()
        form_rand = QFormLayout(page_rand)
        self.rand_xmax_input = QLineEdit("150.0")
        form_rand.addRow("道面长度 x_max:", self.rand_xmax_input)
        self.rand_dx_input = QLineEdit("0.5")
        form_rand.addRow("采样步长 dx:", self.rand_dx_input)
        self.rand_n0_input = QLineEdit("0.1")
        form_rand.addRow("参考频率 n0:", self.rand_n0_input)
        self.rand_Gq_n0_input = QLineEdit("1.64e-6")
        form_rand.addRow("谱密度 Gq_n0:", self.rand_Gq_n0_input)
        self.rand_delt_n_input = QLineEdit("0.0056")
        form_rand.addRow("频率间隔 delt_n:", self.rand_delt_n_input)
        self.stackedWidget.addWidget(page_rand)

        left_layout.addWidget(self.stackedWidget)

        btn_calc_road = QPushButton("生成路面载荷模型")
        btn_calc_road.setMinimumHeight(35)
        btn_calc_road.clicked.connect(self.calcRoadModelEvent)
        left_layout.addWidget(btn_calc_road)

        btn_export_road = QPushButton("导出当前路面数据 (CSV)")
        btn_export_road.setMinimumHeight(35)
        btn_export_road.clicked.connect(self.exportRoadCsvEvent)
        left_layout.addWidget(btn_export_road)
        left_layout.addStretch()

        right_panel = QFrame()
        right_layout = QVBoxLayout(right_panel)
        self.road_fig = Figure(figsize=(6, 5), dpi=100)
        self.road_ax = self.road_fig.add_subplot(111)
        self.road_canvas = FigureCanvas(self.road_fig)
        right_layout.addWidget(self.road_canvas)

        self.modelLibLayout.addWidget(left_panel)
        self.modelLibLayout.addWidget(right_panel)

    def onRoadTypeChanged(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def calcRoadModelEvent(self):
        try:
            self.road_ax.clear()
            is_harmonic = (self.roadTypeCombo.currentIndex() == 0)
            
            if is_harmonic:
                x_max = float(self.harm_xmax_input.text())
                N = int(self.harm_n_input.text())
                L = float(self.harm_L_input.text())
                subtype = self.harm_subtype_combo.currentIndex()
                x = np.linspace(0, x_max, N)
                
                if subtype == 0:
                    y = -83.333 / 2 * (1 - np.cos(np.pi * x / 50))
                    title = "铺砌简谐道面载荷模型"
                elif subtype == 1: 
                    y = -174.6 * (1 - np.cos(np.pi * x / 50))
                    title = "半铺砌简谐道面载荷模型"
                else: 
                    y = -810.45 * (1 - np.cos(np.pi * x / 50)) if L <= 45.72 else 337.3035 * (1 - np.cos(np.pi * x / 50))
                    title = f"未铺砌简谐道面 (L={L}) 载荷模型"

                self.current_road_x, self.current_road_y = x, y
                self.road_ax.plot(x, y, color='#1f77b4')
                self.road_ax.set_title(title, fontweight='bold')
                
            else:
                x_max = float(self.rand_xmax_input.text())
                dx = float(self.rand_dx_input.text())
                n0 = float(self.rand_n0_input.text())
                Gq_n0 = float(self.rand_Gq_n0_input.text())
                delt_n = float(self.rand_delt_n_input.text())
                
                x = np.arange(0, x_max + dx, dx)
                q = np.zeros_like(x)
                thta = 2 * np.pi * np.random.rand(300)
                
                for j in range(1, 301):
                    n = delt_n * (j - 0.5) + 0.011
                    Ai = np.sqrt(2 * (Gq_n0 * (n0**2) / (n**2)) * delt_n)
                    q += Ai * np.sin(2 * np.pi * n * x + thta[j-1])
                
                self.current_road_x, self.current_road_y = x, q
                self.road_ax.plot(x, q, color='#1f77b4', linewidth=1.2)
                self.road_ax.set_title("随机道面载荷模型", fontweight='bold')

            self.road_ax.set_xlabel("位置 x (m)")
            self.road_ax.set_ylabel("高度 (m)")
            self.road_ax.grid(True, linestyle='--', alpha=0.7)
            self.road_canvas.draw()
            
        except ValueError:
            QMessageBox.critical(self, "输入错误", "请检查输入参数是否合法！")

    def exportRoadCsvEvent(self):
        if not hasattr(self, 'current_road_x') or self.current_road_x is None:
            return QMessageBox.warning(self, "警告", "请先生成路面数据！")
        filepath, _ = QFileDialog.getSaveFileName(self, "保存数据", "road_data.csv", "CSV (*.csv)")
        if filepath:
            try:
                with open(filepath, 'w', newline='', encoding='utf-8-sig') as f:
                    w = csv.writer(f)
                    w.writerow(["位置_x", "高度_y"])
                    for x, y in zip(self.current_road_x, self.current_road_y): w.writerow([x, y])
                QMessageBox.information(self, "成功", "导出成功！")
            except Exception as e:
                QMessageBox.critical(self, "失败", str(e))

if __name__ == '__main__':
    dlg = TireAnalysisDialog()
    dlg.setWindowTitle("路面与轮胎载荷分析系统")
    dlg.show()
    sys.exit(app.exec_())