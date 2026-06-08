$ErrorActionPreference = "Stop"

$clang = "C:\Program Files\LLVM\bin\clang.exe"
$inputLl = "output\program.ll"
$outputExe = "output\program.exe"

Write-Host "Buscando librerías de Visual Studio y Windows SDK..."

$vsRoot = "C:\Program Files (x86)\Microsoft Visual Studio\2022"

$msvcLibFile = Get-ChildItem $vsRoot -Filter "libcmt.lib" -Recurse -ErrorAction SilentlyContinue |
    Where-Object { $_.FullName -match "\\lib\\x64\\libcmt\.lib$" } |
    Select-Object -First 1

$oldNamesFile = Get-ChildItem $vsRoot -Filter "oldnames.lib" -Recurse -ErrorAction SilentlyContinue |
    Where-Object { $_.FullName -match "\\lib\\x64\\oldnames\.lib$" } |
    Select-Object -First 1

$ucrtFile = Get-ChildItem "C:\Program Files (x86)\Windows Kits\10\Lib" -Filter "libucrt.lib" -Recurse -ErrorAction SilentlyContinue |
    Where-Object { $_.FullName -match "\\ucrt\\x64\\libucrt\.lib$" } |
    Select-Object -First 1

$kernelFile = Get-ChildItem "C:\Program Files (x86)\Windows Kits\10\Lib" -Filter "kernel32.lib" -Recurse -ErrorAction SilentlyContinue |
    Where-Object { $_.FullName -match "\\um\\x64\\kernel32\.lib$" } |
    Select-Object -First 1

if ($null -eq $msvcLibFile) {
    Write-Host "No se encontró libcmt.lib." -ForegroundColor Red
    exit 1
}

if ($null -eq $oldNamesFile) {
    Write-Host "No se encontró oldnames.lib." -ForegroundColor Red
    exit 1
}

if ($null -eq $ucrtFile) {
    Write-Host "No se encontró libucrt.lib." -ForegroundColor Red
    exit 1
}

if ($null -eq $kernelFile) {
    Write-Host "No se encontró kernel32.lib." -ForegroundColor Red
    exit 1
}

$msvcLibDir = $msvcLibFile.Directory.FullName
$ucrtLibDir = $ucrtFile.Directory.FullName
$umLibDir = $kernelFile.Directory.FullName

Write-Host "MSVC lib: $msvcLibDir"
Write-Host "UCRT lib: $ucrtLibDir"
Write-Host "UM lib:   $umLibDir"
Write-Host ""

Write-Host "Compilando LLVM IR..."

& $clang $inputLl -o $outputExe `
    -Xlinker "/LIBPATH:$msvcLibDir" `
    -Xlinker "/LIBPATH:$ucrtLibDir" `
    -Xlinker "/LIBPATH:$umLibDir"

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "Error al compilar LLVM." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Ejecutando programa:"
& ".\$outputExe"