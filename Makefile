VENV_PATH = 'venv/'

.PHONY: devinstall
devinstall:
	@pip install -r requirements.txt

.PHONY: clean
clean:
	@find . -type d -name __pycache__ -delete
	@find . -type f -name '*.py[co]' -delete
	@rm -rf .coverage
	@rm -rf .pytest_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf docs
	@rm -rf htmlcov
	@rm -rf python_blizzardapi.egg-info

.PHONY: lint
lint:
	@black . --check --exclude $(VENV_PATH)
	@isort . --check --skip $(VENV_PATH)
	@flake8 . --statistics --exclude $(VENV_PATH)

.PHONY: format
format:
	@black . --exclude $(VENV_PATH)
	@isort . --skip $(VENV_PATH)