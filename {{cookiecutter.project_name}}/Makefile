project = {{cookiecutter.project_name}}

# help


# install
install:
	pip install . --ignore-installed

develop:
	pip install -e .

uninstall:
	pip uninstall $(project) -y

# test
test:
	pytest

test-coverage:
	pytest --cov=$(project) --cov-report html --cov-config .coveragerc

# flake8
lint:
	flake8 --exclude=doc,
