@echo off
title MicroOS Launcher
cd /d "C:\Users\M SRIVAS\.gemini\antigravity\scratch\MicroOS\web"

netstat -ano | findstr :8080 >nul
if %errorlevel% neq 0 (
    echo Starting MicroOS server...
    start /b python server.py
    timeout /t 1 /nobreak >nul
)

echo Launching MicroOS Desktop Window...
start "" "msedge.exe" --app=http://localhost:8080 --start-maximized
exit
