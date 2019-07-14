#!/usr/bin/env python3.7

from subprocess import run, PIPE
import datetime
from math import ceil, floor
from time import time, sleep


def main():
    required_coins = fish_price(2391500, 16)
    print(f"required_coins: {int(required_coins/1000)}K")
    current_coins = 5.5 * 10 ** 6
    coins_per_second = 31855
    current_time = floor(time())
    time_of_available_purchase = current_time + ceil(
        float((required_coins - current_coins)) / coins_per_second
    )

    last_time = None
    while current_time < time_of_available_purchase:
        current_time = floor(time())
        if current_time == last_time:
            sleep(0.1)
            continue
        time_left = time_of_available_purchase - current_time
        print(datetime.timedelta(seconds=time_left))
        last_time = current_time

    run(
        "/home/hallgrimur1471/scripts/post_to_slack.py "
        + f"-m='Fish, required_coins: {int(required_coins/1000)}K' "
        + "-c=D859GH2NM -b=abathur",
        shell=True,
    )


def fish_price(initial_fish_price, num_fishes_to_buy):
    r = 1.175  # price of fish increases by r with every purchase
    P = initial_fish_price
    n = num_fishes_to_buy
    total_price = P * ((1 - r ** n) / (1 - r))
    return total_price


if __name__ == "__main__":
    # main()
    print(int(fish_price(409816, 8) / 1))
