from setuptools import setup

project_name = '{{cookiecutter.project_name}}'
author = '{{cookiecutter.author_name}}'

install_requires = ['PyYAML']
extras_require = {
    'test': ['pytest', 'flake8', 'pytest-cov'],
}

setup(
    name=project_name,
    version='0.1',
    author=author,
    # packagesは指定する必要あり
    packages=['{{cookiecutter.project_name}}'],
    install_requires=install_requires,
    extras_require=extras_require)
