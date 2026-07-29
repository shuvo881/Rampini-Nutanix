#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd "$SCRIPT_DIR/backend"

if command -v uv >/dev/null 2>&1; then
  UV=uv
else
  UV=python
fi

$UV run main.py &
backend_pid=$!
trap 'kill "$backend_pid" 2>/dev/null || true' EXIT

cd "$SCRIPT_DIR/frontend"
npm run dev

wait "$backend_pid"
