project = {{cookiecutter.project_name}}

# help
## helpはhttps://postd.cc/auto-documented-makefile/を参考にした
.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

DEFAULT_GOAL := help

# install
install: ## Install python project.(Ignore the installed packages (reinstalling instead).)
	pip install . --ignore-installed

develop: ## Install a project in editable mode (i.e. setuptools "develop mode") from a local project path or a VCS url.
	pip install -e .

uninstall: ## installしたpackageを削除
	pip uninstall $(project) -y

# test
test: ## pytestによるtest実行
	pytest

test-coverage: ## coverageを計測し、htmlに出力
	pytest --cov=$(project) --cov-report html --cov-config .coveragerc


# flake8
lint: ## flake8のlint実行
	flake8 --exclude=doc,

# clean
clean: clean-pyc uninstall ## .pyc系のファイル削除とuninstallの実行

# cf. https://qiita.com/iron-breaker/items/74a2ed1753587476157f
clean-pyc: ## .pyc[o]や__pycache__を削除
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +

# clean-dist:
# 	rm -rf build/
# 	rm -rf dist/
# 	rm -rf $(project).egg-info
