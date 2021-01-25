.PHONY: devinstall
devinstall:
	pip install -r requirements.txt

.PHONY: clean
clean:
	find . -type d -name __pycache__ -delete
	find . -type f -name '*.py[co]' -delete
	rm -rf .coverage
	rm -rf .pytest_cache
	rm -rf build
	rm -rf dist
	rm -rf docs
	rm -rf htmlcov
	rm -rf .mypy_cache
	rm -rf python_blizzardapi.egg-info

.PHONY: lint
lint:
	black blizzardapi --check
	bandit blizzardapi
	flake8 blizzardapi --statistics
	isort blizzardapi --check
	mypy blizzardapi
	pydocstyle blizzardapi
	pylint blizzardapi --exit-zero

.PHONY: format
format:
	black blizzardapi
	isort blizzardapi