@echo off
echo ========================================
echo NKU Thesis Build Script
echo ========================================

echo.
echo [1/4] XeLaTeX pass 1...
xelatex main
if %errorlevel% neq 0 (
    echo Error: XeLaTeX failed
    pause
    exit /b 1
)

echo.
echo [2/4] Biber...
biber main
if %errorlevel% neq 0 (
    echo Error: Biber failed
    pause
    exit /b 1
)

echo.
echo [3/4] XeLaTeX pass 2...
xelatex main
if %errorlevel% neq 0 (
    echo Error: XeLaTeX failed
    pause
    exit /b 1
)

echo.
echo [4/4] XeLaTeX pass 3...
xelatex main
if %errorlevel% neq 0 (
    echo Error: XeLaTeX failed
    pause
    exit /b 1
)

echo.
echo [Clean] Removing auxiliary files...
del /q *.aux *.out *.blg *.toc *.bbl *.bcf 2>nul

echo.
echo ========================================
echo Build complete! main.pdf generated.
echo ========================================
pause
