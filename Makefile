.PHONY: devinstall clean lint

devinstall:
	pip install -r requirements.txt

clean:
	rm -rf dist
	rm -rf build
	rm -rf htmlcov
	rm -rf python_blizzardapi.egg-info
	rm -rf .coverage
	rm -rf docs
	rm -rf .pytest_cache
	find . -type f -name '*.py[co]' -delete
	find . -type d -name __pycache__ -delete

lint:
	black . -l 200 && black . -l 79
	bandit blizzardapi
	mypy blizzardapi
	pycodestyle blizzardapi
	pydocstyle blizzardapi
	pyflakes blizzardapi
	pylint blizzardapi