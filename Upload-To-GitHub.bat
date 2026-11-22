@echo off
setlocal
cd /d "C:\Users\M SRIVAS\.gemini\antigravity\scratch\MicroOS"

echo ============================================================
echo           MicroOS - Automated GitHub Publisher
echo ============================================================
echo Student  : M. Srivas (USN: 25BTRCL143)
echo College  : Jain University (FET) - AIML
echo Username : juug25btech19864-hash
echo Repo Name: MicroOS
echo Target   : https://github.com/juug25btech19864-hash/microOS2
echo Location : %CD%
echo ============================================================
echo.

git branch -M main
git remote remove origin 2>nul
git remote add origin https://github.com/juug25btech19864-hash/microOS2.git

echo [*] Staging all project files...
git add .
git status --short

echo [*] Committing latest changes...
git commit -m "release(v1.0): Complete MicroOS ultra-lightweight Linux OS and GUI Desktop Edition - M. Srivas (25BTRCL143)" 2>nul

echo [*] Pushing to GitHub...
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ============================================================
    echo   MICROOS SUCCESSFULLY PUBLISHED TO GITHUB!
    echo ============================================================
    echo   GitHub URL: https://github.com/juug25btech19864-hash/microOS2
    echo ============================================================
) else (
    echo.
    echo [!] Push failed. Please verify your credentials or Personal Access Token.
)

echo.
pause
