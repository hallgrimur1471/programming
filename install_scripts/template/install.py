#!/usr/bin/env python3.7

import os
import os.path
import argparse
import urllib.request
import json
import subprocess


def main():
    args = parse_arguments()
    install_prerequisites()
    install_project()
    if not args.dont_install_configs:
        install_configs()
    tprint("done")


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.description = ""
    parser.add_argument("--dont-install-configs", help="")
    arguments = parser.parse_args()
    return arguments


def install_prerequisites():
    tprint("installing prerequisites ...")
    install_apt_dependencies([])
    install_pip_dependencies([])


def install_project():
    tprint("installing project ...")
    pass  # Not implemented


def install_configs():
    tprint("installing configs ...")
    pass  # Not implemented


def install_apt_dependencies(apt_dependencies):
    for dependency in apt_dependencies:
        try_cmd(f"sudo apt-get install -y {dependency}")


def install_pip_dependencies(pip_dependencies):
    for dependency in pip_dependencies:
        try_cmd(f"python3 -m pip install --user {dependency}")


def get_project_root_dir():
    dn = os.path.dirname
    project_root_dir = dn(os.path.abspath(__file__))
    return project_root_dir


def open_url(url):
    http_response = urllib.request.urlopen(url)
    body_string = http_response.read().decode()
    return body_string


def tprint(*args, **kwargs):
    this_file = os.path.basename(__file__)
    print(f"[{this_file}]:", *args, flush=True, **kwargs)


def try_cmd(*args, **kwargs):
    completed_process = cmd(*args, **kwargs)

    if completed_process.returncode != 0:
        command = args[0]

        error_msg = (
            f"{command} failed with return code {completed_process.returncode}."
        )
        if completed_process.stdout or completed_process.stderr:
            error_msg += "\n"
        if completed_process.stdout:
            error_msg += f"\nHere is its stdout:\n{completed_process.stdout}"
        if completed_process.stderr:
            error_msg += f"\nHere is its stderr:\n{completed_process.stderr}"

        raise RuntimeError(error_msg)


def cmd(*args, **kwargs):
    if "shell" not in kwargs:
        kwargs["shell"] = True
    if "executable" not in kwargs:
        kwargs["executable"] = "/bin/bash"

    if "dont_print_command" not in kwargs:
        command = args[0]
        tprint(f"$ {command}")

    completed_process = subprocess.run(*args, **kwargs)
    return completed_process


if __name__ == "__main__":
    main()


# Unit tests, invoke by running `pytest install.py` #


def test_something():
    pass  # Not implemented
