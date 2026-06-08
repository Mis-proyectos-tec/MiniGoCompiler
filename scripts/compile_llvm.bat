@echo off

call "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\Common7\Tools\VsDevCmd.bat" -arch=x64 -host_arch=x64 >nul 2>&1

"C:\Program Files\LLVM\bin\clang.exe" output\program.ll -o output\program.exe >nul

if errorlevel 1 (
    echo Error al compilar LLVM.
    exit /b 1
)

output\program.exe