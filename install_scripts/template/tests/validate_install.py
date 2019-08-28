#!/usr/bin/env python3.7

import argparse
import subprocess
import os.path
import sys

import pytest


def main():
    args = parse_arguments()
    is_valid = validate_install()

    if is_valid:
        sys.exit(0)
    else:
        sys.exit(1)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.description = ""
    arguments = parser.parse_args()
    return arguments


def validate_install():
    exit_code = run_pytest_on_this_file()

    if exit_code == pytest.ExitCode.OK:
        is_valid = True
    else:
        is_valid = False

    return is_valid


def run_pytest_on_this_file():
    this_file = os.path.abspath(__file__)
    exit_code = pytest.main([this_file])
    return exit_code


# TESTS #


def test_project_is_installed():
    assert 0 # not implemented


def test_project_config_files_are_deployed():
    assert 0 # not implemented


if __name__ == "__main__":
    main()
