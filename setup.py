# This script is used to package and distribute the project.
# Example:

from setuptools import setup, find_packages

setup(
    name="my_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "mysql-connector-python"
    ],
    entry_points={
        "console_scripts": [
            "my_project=my_project.main:main"
        ]
    },
)

# Install package locally using: pip install -e .
