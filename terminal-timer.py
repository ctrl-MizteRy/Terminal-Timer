#!/usr/bin/env python3
import argparse
import subprocess
from time import sleep

def main():
    args = argparse.ArgumentParser()
    args.add_argument("--start", action="store_true", help="starting the timmer")
    args.add_argument("-sec", type=check_value, default=0, help="The amount of seconds")
    args.add_argument("-min", type=check_value, default=0, help="The amount of minutes")
    args.add_argument("-hour", type=check_value, default=0, help="The amount of hours")

    argv = args.parse_args()
    if argv.start:
        total = int(argv.sec) + (60* int(argv.min)) + (3600 * int(argv.hour))
        if total == 0:
            print("Cannot start a timer for 0 seconds")
            exit(0)
        else:
            print(f"Starting a timer for {total} seconds")
            sleep(total)
            time_up()
    
    else:
        print("Missing Command-line Arguemnt")
        

def check_value(value):
    try:
        n = int(value)
        if n < 0:
            raise argparse.ArgumentError("Number need to be possitive")
        return n        
    
    except TypeError:
        raise argparse.ArgumentError("%s need to be an Integer" %value)
    
def time_up():
    command = '/usr/games/cowsay "Time is up"'
    subprocess.Popen(["tilix", "--", "bash", "-c", command])


if __name__ == "__main__":
    main()