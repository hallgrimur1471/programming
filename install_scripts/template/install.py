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
    parser.add_argument(
        "--dont-install-configs", help=""
    )
    arguments = parser.parse_args()
    return arguments


def install_prerequisites():
    tprint("installing prerequisites ...")
    apt_dependencies = []
    for dependency in apt_dependencies:
        subprocess.run(f"sudo apt-get install -y {dependency}", shell=True)


def install_project():
    tprint("installing project ...")
    pass # Not implemented

def install_configs():
    tprint("installing configs ...")
    pass # Not implemented

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

if __name__ == "__main__":
    main()


# Unit tests, invoke by running `pytest install.py` #


def test_something():
    pass # Not implemented
