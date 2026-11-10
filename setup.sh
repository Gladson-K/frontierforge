#!/usr/bin/env bash
set -euo pipefail
PYTHON=${PYTHON:-python3}
$PYTHON - <<'PY'
import sys
if sys.version_info < (3,10): raise SystemExit('Python 3.10+ is required')
print('Python',sys.version.split()[0])
PY
$PYTHON -m venv .venv
.venv/bin/python -m pip install --upgrade pip
printf '\nFrontierForge environment ready. Run: .venv/bin/python -m frontierforge.cli --help\n'
