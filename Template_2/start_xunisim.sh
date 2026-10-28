#!/bin/bash
# The toolbar passes the installation path as one argument.
set -eu

if [[ "$#" -ne 1 ]]; then
    printf 'Usage: bash start_xunisim.sh /absolute/path/to/XUnisim-Application\n' >&2
    exit 2
fi

program="$1"
if [[ ! -f "$program" ]]; then
    printf 'Xunisim program not found: %s\n' "$program" >&2
    exit 127
fi
if [[ ! -x "$program" ]]; then
    printf 'Xunisim program is not executable: %s\n' "$program" >&2
    exit 126
fi

log_dir="${XDG_STATE_HOME:-$HOME/.local/state}/fmbs"
mkdir -p -- "$log_dir"
exec >> "$log_dir/xunisim.log" 2>&1
printf '\n--- Xunisim launch: %s ---\n' "$(date '+%Y-%m-%d %H:%M:%S')"
cd -- "$(dirname -- "$program")"

# Add vendor-required environment initialization here, if needed.
exec "$program"
