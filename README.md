### Python installation
```commandline
brew update
brew install uv
uv python install 3.12
# change directory to this folder
uv venv
```

### Install dependencies and activate virtual environment
```commandline
uv pip install -r pyproject.toml
```

### Run tests
```commandline
uv run pytest
```