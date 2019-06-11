#!/usr/bin/env python3.7

import argparse
import os
import os.path
from os.path import abspath, dirname, basename
from pathlib import Path
import shutil

DEBUG = "OFF"


def main():
    args = parse_arguments()

    beutified_package_path = (
        Path(abspath(args.PACKAGE_DIR).replace(os.environ["HOME"], "~"))
        / args.PACKAGE_NAME
    )
    print(f"Setting up a basic python package at {beutified_package_path}")
    func_args = [
        args.PYTHON_VERSION,
        args.PACKAGE_NAME,
        args.GITHUB_USERNAME,
        Path(args.PACKAGE_DIR),
    ]
    func_kwargs = dict()
    if args.application_name:
        setup_package_kwargs["application_name"] = args.application_name
    setup_package(*func_args, **func_kwargs)
    print("Package setup complete.")


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.description = (
        "Sets up a basic Python package in PACKAGE_DIR/PACKAGE_NAME"
    )
    parser.add_argument("PYTHON_VERSION", help="Example: 3.7")
    parser.add_argument("PACKAGE_NAME", help="Name of package")
    parser.add_argument("GITHUB_USERNAME", help="Your username on Github")
    parser.add_argument(
        "PACKAGE_DIR",
        help="The directory which the package should be created in. Example: ~",
    )
    parser.add_argument(
        "--application-name",
        help=(
            "Main application to be run (name without extension), "
            "defaults to 'main'"
        ),
    ),
    arguments = parser.parse_args()
    return arguments


def setup_package(
    python_version,
    package_name,
    github_username,
    package_dir,
    application_name="main",
):
    project_dir = Path(dirname(abspath(__file__)))
    core_dir = project_dir / "core"
    dest_dir = package_dir / package_name

    package_name_header = package_name[0].upper() + package_name[1:]
    package_name_header = package_name_header.replace("_", " ")
    replacement_dict = {
        "{PYTHON_VERSION}": python_version,
        "{PACKAGE_NAME}": package_name,
        "{PACKAGE_NAME_HEADER}": package_name_header,
        "{GITHUB_USERNAME}": github_username,
        "{PACKAGE_DIR}": package_dir,
        "{APPLICATION_NAME}": application_name,
    }
    replacement_keys = list(replacement_dict.keys())

    # clean MyPy cache from core
    mypy_cache_dir = core_dir / ".mypy_cache"
    if os.path.exists(mypy_cache_dir):
        shutil.rmtree(mypy_cache_dir)

    # copy core
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    shutil.copytree(core_dir, dest_dir)

    # rename files
    for dirpath, dirnames, filenames in os.walk(dest_dir, topdown=False):
        for file_ in filenames:
            for key in replacement_keys:
                file_key = key.replace("{", "").replace("}", "")
                if file_key in file_:
                    new_file = file_.replace(file_key, replacement_dict[key])
                    src = Path(dirpath) / file_
                    dest = Path(dirpath) / new_file
                    dbg(f"Renaming '{src}' to '{dest}'")
                    os.rename(src, dest)
        for dir_ in dirnames:
            for key in replacement_keys:
                dir_key = key.replace("{", "").replace("}", "")
                if dir_key in dir_:
                    new_dir = dir_.replace(dir_key, replacement_dict[key])
                    src = Path(dirpath) / dir_
                    dest = Path(dirpath) / new_dir
                    dbg(f"Renaming '{src}' to '{dest}'")
                    os.rename(src, dest)

    # replace file data
    for dirpath, dirnames, filenames in os.walk(dest_dir):
        for file_ in filenames:
            file_path = Path(dirpath) / file_
            file_lines = None
            with open(file_path, "r") as fh:
                file_lines = fh.readlines()
            new_file_lines = []
            for i, line in enumerate(file_lines):
                new_line = line
                for key in replacement_keys:
                    if key in new_line:
                        dbg(
                            f"Replacing '{key}' by '{replacement_dict[key]}' "
                            f"in '{basename(file_path)}' line {i+1}"
                        )
                        new_line = new_line.replace(key, replacement_dict[key])
                new_file_lines.append(new_line)
            with open(file_path, "w") as fh:
                for line in new_file_lines:
                    fh.write(line)


def dbg(*args, **kwargs):
    if DEBUG == "ON":
        print("DEBUG: ", end="")
        print(*args, **kwargs)


if __name__ == "__main__":
    main()
