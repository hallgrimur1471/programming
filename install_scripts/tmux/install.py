#!/usr/bin/env python3.7

import argparse


def main():
    args = parse_arguments()


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.description = "Convert *nix path to Windows-like path"
    parser.add_argument("PATH", help="*nix path to be converted.")
    arguments = parser.parse_args()
    return arguments


if __name__ == "__main__":
    main()
