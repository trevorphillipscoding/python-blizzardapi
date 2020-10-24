devinstall:
	pip install -e .
	pip install -e .[tests]

clean:
	rm -rf dist
	rm -rf build
	rm -rf htmlcov
	rm -rf python_blizzardapi.egg-info
	rm -rf .coverage
	rm -rf docs
	rm -rf .pytest_cache
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete