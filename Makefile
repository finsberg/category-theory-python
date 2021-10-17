.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	rm -f src/category_theory/cost_terms.*

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style with flake8
	python -m flake8 src/category_theory tests

type: ## Run mypy
	python3 -m mypy src/category_theory tests

test: ## run tests on every Python version with tox
	python3 -m pytest

spell: ## Run spell checker
	 cspell-cli lint src/category_theory/* -c cspell.config.yaml --color

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/source/category_theory.rst
	rm -f docs/source/modules.rst
	for file in README.md; do \
		cp $$file docs/. ;\
	done
	sphinx-apidoc -o docs/source src/category_theory
	$(MAKE) -C docs clean
	$(MAKE) -C docs html

release: dist ## package and upload a release
	python3 -m twine upload -u ${PYPI_USERNAME} -p ${PYPI_PASSWORD} dist/*

dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	python3 -m pip install .

dev: clean ## Just need to make sure that libfiles remains
	python3 -m pip install -e ".[dev]"
	pre-commit install

bump:  ## Bump version
	bump2version patch
