#!/usr/bin/env python3

import time


def main():
    if next_event_is_break():
        wait_until_break()
        run_break_alert()

    while True:
        wait_until_break_is_over()
        run_break_over_alert()

        wait_until_break()
        run_break_alert()


def next_event_is_break():
    minute = get_current_minute()
    return should_be_working_during(minute)


def get_current_minute():
    current_minute = time.localtime().tm_min
    return current_minute


def should_be_working_during(minute):
    if (5 <= minute and minute < 30) or (35 <= minute):
        return True
    return False


def wait_until_break():
    while should_be_working_during(get_current_minute()):
        time.sleep(0.2)


def wait_until_break_is_over():
    while not should_be_working_during(get_current_minute()):
        time.sleep(0.2)


def run_break_alert():
    tprint("It's time for a break!")


def run_break_over_alert():
    tprint("It's time to start working again!")


def tprint(*args, **kwargs):
    print("[{}]".format(time.localtime()), *args, **kwargs)


if __name__ == "__main__":
    main()
    current_minute = get_current_minute()
