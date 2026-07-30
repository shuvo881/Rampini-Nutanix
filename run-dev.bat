@echo off
REM Run backend and frontend from repo root.
set SCRIPT_DIR=%~dp0

REM Start backend in a new terminal window.
start "" cmd /k "cd /d "%SCRIPT_DIR%backend" && uv run main.py"

REM Run frontend in this window.
cd /d "%SCRIPT_DIR%frontend"
npm run dev
