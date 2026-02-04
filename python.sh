#!/usr/bin/env bash

# Check if uv command exists
if command -v uv &> /dev/null; then
    # uv exists, forward arguments to uv run
    uv run python "$@"
else
    # uv does not exist, download and install it
    echo "uv not found. Installing uv..."

    # Install uv using official installer
    curl -LsSf https://astral.sh/uv/install.sh | sh

    # Refresh PATH
    if [[ -n "$XDG_BIN_HOME" ]]; then
        export PATH="$XDG_BIN_HOME:$PATH"
    elif [[ -n "$XDG_DATA_HOME" ]]; then
        export PATH="$XDG_DATA_HOME/../bin:$PATH"
    else
        export PATH="$HOME/.local/bin:$PATH"
    fi

    # Forward arguments to uv run
    uv run python "$@"
fi
