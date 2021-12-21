#!/usr/bin/env python3

import requests
import sys
import argparse


def main():
    args = parse_args()
    inpt = get_input(args.YEAR, args.DAY, args.COOKIE)
    sys.stdout.write(inpt)


def get_input(year, day, cookie):
    headers = {"session": cookie}
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    session = requests.Session()
    response = session.get(url, cookies=headers)
    return response.text


def parse_args():
    parser = argparse.ArgumentParser()
    parser.description = "Fetches and prints input for AoC problem"
    parser.add_argument("YEAR", help="Year of the AoC problem, example: 2018")
    parser.add_argument("DAY", help="a number from 1-25. Fetch input for DAY")
    parser.add_argument(
        "COOKIE",
        help=(
            "session cookie for your log-in session "
            "on AoC, look it up in your brower"
        ),
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()
