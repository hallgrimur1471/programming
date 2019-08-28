#!/usr/bin/env python3.7

import argparse


def main():
    args = parse_arguments()


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.description = ""
    arguments = parser.parse_args()
    return arguments


if __name__ == "__main__":
    main()
