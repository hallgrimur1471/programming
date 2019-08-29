#!/usr/bin/env python3.7

import argparse
import subprocess
import sys
import os.path


def main():
    args = parse_arguments()
    make_sure_that_docker_is_installed()
    build_tester_container()
    returncode = run_tester_container()
    sys.exit(returncode)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.description = (
        "Runs install.py in a Docker container and then runs "
        + "tests/validate_install.py to validate that install.py "
        + "installed the project correctly"
    )
    arguments = parser.parse_args()
    return arguments


def make_sure_that_docker_is_installed():
    tprint("making sure docker is installed ...")
    completed_process = subprocess.run(
        "docker --version", shell=True, stdout=subprocess.PIPE
    )
    if completed_process.returncode != 0:
        raise RuntimeError("It seems like docker is not installed")


def build_tester_container():
    project_root_dir = get_project_root_dir()
    container_name = determine_container_name()

    tprint(f"building container {container_name} ...")
    completed_process = subprocess.run(
        f"docker build -t {container_name} {project_root_dir}", shell=True
    )
    if completed_process.returncode != 0:
        raise RuntimeError(f"Failed to build {container_name} docker container")


def run_tester_container():
    container_name = determine_container_name()
    tprint(f"running container {container_name} ...")
    completed_process = subprocess.run(
        f"docker run {container_name}", shell=True
    )
    return completed_process.returncode


def get_project_root_dir():
    dn = os.path.dirname
    project_root_dir = dn(dn(os.path.abspath(__file__)))
    return project_root_dir


def determine_container_name():
    project_root_dir = get_project_root_dir()
    container_name = "{}_installation_script_tester".format(
        os.path.basename(project_root_dir)
    )
    return container_name


def tprint(*args, **kwargs):
    this_file = os.path.basename(__file__)
    print(f"[{this_file}]:", *args, flush=True, **kwargs)


if __name__ == "__main__":
    main()
