#!/usr/bin/env pwsh

# Check if uv command exists
if (Get-Command uv -ErrorAction SilentlyContinue) {
    # uv exists, forward arguments to uv run
    uv run python @args
} else {
    # uv does not exist, download and install it
    Write-Host "uv not found. Installing uv..."
    
    # Download and install uv using the official installer
    Invoke-Expression "& { $(Invoke-RestMethod https://astral.sh/uv/install.ps1) }"

    # Refresh PATH for current session
    if ($env:XDG_BIN_HOME) {
        $uvInstallDir = $env:XDG_BIN_HOME
    } elseif ($env:XDG_DATA_HOME) {
        $uvInstallDir = Join-Path $env:XDG_DATA_HOME "..\bin"
    } else {
        $uvInstallDir = Join-Path $env:USERPROFILE ".local\bin"
    }

    if ($env:PATH -notlike "*$uvInstallDir*") {
        $env:PATH = "$uvInstallDir;$env:PATH"
    }
    
    # Forward arguments to uv run
    uv run python @args
}
