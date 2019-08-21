#!/usr/bin/env python3

import time
import os.path

import playsound


def main():
    if should_be_working_now():
        tprint("Waiting until next break ...")
        wait_until_break()
        run_break_alert()

    while True:
        tprint("Waiting until break is over ...")
        wait_until_break_is_over()
        run_break_over_alert()

        tprint("Waiting until next break ...")
        wait_until_break()
        run_break_alert()


def should_be_working_now():
    minute = get_current_minute()
    return should_be_working_during(minute)


def get_current_minute():
    return time.localtime().tm_min


def should_be_working_during(minute):
    return (5 <= minute and minute < 30) or (35 <= minute)


def tprint(*args, **kwargs):
    current_time = time.localtime()
    current_time_str = time.strftime("%H:%M:%S", current_time)
    print("[{}]:".format(current_time_str), *args, **kwargs)


def wait_until_break():
    wait_until(lambda: not should_be_working_now())


def wait_until(criteria_is_met):
    while not criteria_is_met():
        time.sleep(0.2)


def run_break_alert():
    tprint("It's time for a break!")
    play_sound("stage_clear.mp3")


def play_sound(sound_file_name):
    project_root_dir = get_project_root_dir()
    playsound.playsound(
        os.path.join(project_root_dir, "sounds/{}".format(sound_file_name))
    )


def get_project_root_dir():
    project_root_dir = os.path.dirname(os.path.abspath(__file__))
    return project_root_dir


def wait_until_break_is_over():
    wait_until(lambda: should_be_working_now())


def run_break_over_alert():
    tprint("It's time to start working again!")
    play_sound("airship_clear.mp3")


if __name__ == "__main__":
    main()