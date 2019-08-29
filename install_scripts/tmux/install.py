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
    install_tmux()
    if not args.dont_install_configs:
        install_configs()
    tprint("done")


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.description = ""
    parser.add_argument(
        "--dont-install-configs",
        help="Don't install configs/tmux_v2_9.conf to ~/.tmux.conf"
    )
    arguments = parser.parse_args()
    return arguments


def install_prerequisites():
    tprint("installing prerequisites ...")
    apt_dependencies = ["libevent-dev", "libncurses5-dev"]
    for dependency in apt_dependencies:
        subprocess.run(f"sudo apt-get install -y {dependency}", shell=True)


def install_tmux():
    tprint("installing tmux ...")
    latest_release_url = find_url_to_latest_release()
    install_tmux_from_url(latest_release_url)

def install_configs():
    tprint("installing configs ...")
    project_root_dir = get_project_root_dir()
    config_file = "configs/tmux_v2_9.conf"
    config_file_path = os.path.join(project_root_dir, config_file)
    destination = os.path.join(os.environ['HOME'], '.tmux.conf')

    subprocess.run(f"cp {config_file_path} {destination}", shell=True)

def find_url_to_latest_release():
    version_tag = find_version_tag_of_latest_release()
    url_to_latest_release_tarball = calculate_url_to_latest_release_tarball(
        version_tag
    )
    return url_to_latest_release_tarball


def install_tmux_from_url(tarball_url):
    version_tag = find_version_tag_of_latest_release()
    tarball_file_name = f"tmux-{version_tag}.tar.gz"

    tarball_download_location = f"{os.environ['HOME']}/{tarball_file_name}"

    subprocess.run(
        f"cd ~ && "
        + f"curl -L -o {tarball_download_location} {tarball_url} && "
        + f"tar -xzf {tarball_file_name} && "
        + f"cd {tarball_file_name.replace('.tar.gz', '')} && "
        + f"./configure && "
        + f"make && "
        + f"sudo make install",
        shell=True,
    )

def get_project_root_dir():
    dn = os.path.dirname
    project_root_dir = dn(os.path.abspath(__file__))
    return project_root_dir


def find_version_tag_of_latest_release():
    response = open_url(
        "https://api.github.com/repos/tmux/tmux/releases/latest"
    )
    response_dict = json.loads(response)
    version_tag = response_dict["tag_name"]
    return version_tag


def calculate_url_to_latest_release_tarball(version_tag):
    url_to_latest_release_tarball = (
        f"https://github.com/tmux/tmux/releases/download"
        f"/{version_tag}/tmux-{version_tag}.tar.gz"
    )
    return url_to_latest_release_tarball


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


def test_calculate_url_to_latest_release_tarball():
    calculated_url = calculate_url_to_latest_release_tarball("2.9a")
    assert (
        calculated_url
        == "https://github.com/tmux/tmux/releases/download/2.9a/tmux-2.9a.tar.gz"
    )


def test_find_url_to_latest_release():
    assert "https" in find_url_to_latest_release()
