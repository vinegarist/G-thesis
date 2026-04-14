@echo off
chcp 65001 >nul
echo ========================================
echo 南开大学论文模板编译脚本
echo ========================================

echo.
echo [1/4] 第一遍 XeLaTeX 编译...
xelatex main
if %errorlevel% neq 0 (
    echo 错误: XeLaTeX 编译失败
    pause
    exit /b 1
)

echo.
echo [2/4] Biber 处理参考文献...
biber main
if %errorlevel% neq 0 (
    echo 错误: Biber 处理失败
    pause
    exit /b 1
)

echo.
echo [3/4] 第二遍 XeLaTeX 编译...
xelatex main
if %errorlevel% neq 0 (
    echo 错误: XeLaTeX 编译失败
    pause
    exit /b 1
)

echo.
echo [4/4] 第三遍 XeLaTeX 编译...
xelatex main
if %errorlevel% neq 0 (
    echo 错误: XeLaTeX 编译失败
    pause
    exit /b 1
)

echo.
echo [清理] 删除辅助文件...
del /q *.aux *.out *.blg *.toc *.bbl *.bcf 2>nul

echo.
echo ========================================
echo 编译完成！生成 main.pdf
echo ========================================
pause
