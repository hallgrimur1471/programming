#!/usr/bin/env python3.7

import argparse
import os.path
from os.path import abspath, join, basename
import Pathlib


def main():
    args = parse_arguments()


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.description = ""
    # parser.add_argument("PATH", help="")
    arguments = parser.parse_args()
    return arguments


if __name__ == "__main__":
    main()
