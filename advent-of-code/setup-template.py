#!/usr/bin/env python3

import sys
import time

def main():
    start_time = time.time()

    end_time = time.time()
    print("runtime: "+seconds_to_hms(end_time-start_time))

def seconds_to_hms(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

def error(msg):
    sys.stdout.write("Error: "+msg+"\n")
    sys.exit(1)

if __name__ == "__main__":
    main()
