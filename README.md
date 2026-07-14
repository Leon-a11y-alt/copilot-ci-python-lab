# Copilot Python CI Lab

A small Python project demonstrating continuous integration with GitHub Actions.

The workflow runs on every push and pull request. It installs the dependencies
with pip caching enabled, checks the code with Flake8, and runs the pytest test
suite.

## Run locally

Python 3.10 or newer is required.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
flake8 src tests
pytest
```
