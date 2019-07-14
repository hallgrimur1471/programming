#!/usr/bin/env python3.7
# pylint: disable=invalid-name

import setuptools
from os.path import abspath, dirname
from pathlib import Path

project_dir = Path(dirname(abspath(__file__)))

with open(project_dir / "README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="{PACKAGE_NAME}",
    version="1.0",
    author="Hallgrimur David Egilsson",
    author_email="hallgrimur1471@gmail.com",
    description="The {PACKAGE_NAME_HEADER} package",
    long_description=long_description,
    url="https://github.com/{GITHUB_USERNAME}/{PACKAGE_NAME}",
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: {PYTHON_VERSION}"],
)
