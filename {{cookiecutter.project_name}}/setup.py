from setuptools import setup

project_name = '{{cookiecutter.project_name}}'
author = '{{cookiecutter.author_name}}'

setup(
    name=project_name,
    version='0.1',
    author=author,
    # packagesは指定する必要あり
    packages=['{{cookiecutter.project_name}}'])
