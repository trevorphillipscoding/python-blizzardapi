.PHONY: devinstall clean lint

devinstall:
	pip install -r requirements.txt

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

lint:
	black . -l 200 && black . -l 79
	bandit blizzardapi
	mypy blizzardapi
	pydocstyle blizzardapi
	pylint blizzardapi --exit-zero