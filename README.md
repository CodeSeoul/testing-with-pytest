### Python installation
```commandline
brew update
brew install pyenv
pyenv install 3.12.0
# change directory to this folder
pyenv local 3.12.0
```

### Install dependencies and activate virtual environment
```commandline
pip install pipenv
pipenv install --dev
pipenv shell
```

### Run tests
```commandline
pipenv run pytest
```