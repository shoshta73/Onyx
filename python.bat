@echo off
setlocal enabledelayedexpansion

REM Check if uv command exists
where uv >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    REM uv exists, forward arguments to uv run
    uv run python %*
) else (
    REM uv does not exist, download and install it
    echo uv not found. Installing uv...
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

    REM Refresh PATH based on XDG spec
    if not "%XDG_BIN_HOME%"=="" (
        if exist "%XDG_BIN_HOME%\uv.exe" (
            set "PATH=%PATH%;%XDG_BIN_HOME%"
        )
    ) else if not "%XDG_DATA_HOME%"=="" (
        if exist "%XDG_DATA_HOME%\..\bin\uv.exe" (
            set "PATH=%PATH%;%XDG_DATA_HOME%\..\bin"
        )
    ) else if exist "%USERPROFILE%\.local\bin\uv.exe" (
        set "PATH=%PATH%;%USERPROFILE%\.local\bin"
    )

    REM Forward arguments to uv run
    uv run python %*
)
