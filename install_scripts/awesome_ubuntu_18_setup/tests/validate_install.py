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

# run_install_scripts(
#    [
#        "python/ubuntu_18/install.sh",
#        "essentials/install.py",
#        "ultimate_vim_configuration/install.py",
#        "tmux/install.py",
#        "sublime_text_3/install.py",
#    ]
# )


def test_python_is_installed():
    assert_program_is_installed("python3.7")


def test_git_is_installed():
    assert_program_is_installed("git")


def test_vim_is_installed():
    assert_program_is_installed("vim")


def test_tmux_is_installed():
    assert_program_is_installed("tmux")


def test_sublime_text_3_is_installed():
    assert_program_is_installed("subl")


def test_git_username_is_configured():
    completed_process = subprocess.run(
        "git config user.name", shell=True, stdout=subprocess.PIPE
    )
    assert completed_process.stdout.decode().rstrip() != ""


def test_git_email_is_configured():
    completed_process = subprocess.run(
        "git config user.email", shell=True, stdout=subprocess.PIPE
    )
    assert completed_process.stdout.decode().rstrip() != ""


def assert_program_is_installed(program):
    completed_process = subprocess.run(
        f"which {program}", shell=True, stdout=subprocess.PIPE
    )
    assert completed_process.returncode == 0


if __name__ == "__main__":
    main()
