@echo off
echo Healthcare Portal - Windows Setup
echo ================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.11+ from https://python.org
    pause
    exit /b 1
)

echo Running automated setup...
python setup-local.py

if errorlevel 1 (
    echo.
    echo Setup failed. Please check the error messages above.
    pause
    exit /b 1
)

echo.
echo Setup complete! To start the application:
echo 1. Run: venv\Scripts\activate
echo 2. Run: python main.py
echo 3. Open: http://localhost:5000
echo.
pause