#!/usr/bin/env python3
import argparse
from time import sleep
from playsound import playsound
import sys
import schedule
import os

def main():
    args = argparse.ArgumentParser()
    args.add_argument("--start", action="store_true", help="starting the timer")
    args.add_argument("-sec", type=check_value, default=0, help="The amount of seconds")
    args.add_argument("-min", type=check_value, default=0, help="The amount of minutes")
    args.add_argument("-hour", type=check_value, default=0, help="The amount of hours")
    args.add_argument("-time", type=check_value, default=0, help="Select specific time the alarm go off in the format of 'hhmm' in 24hrs")
    argv = args.parse_args()
    if argv.start:
        try:
            if argv.time > 0:
                if argv.time < 1000:
                    time_at = "0" + str(argv.time)[:2] + ":" + str(argv.time)[1:]
                else:
                    time_at = str(argv.time)[:2] + ":" + str(argv.time)[2:]
                schedule.every().day.at(time_at).do(time_up)
                print(f"Set alarm for {time_at}")
                while True:
                    schedule.run_pending()
                    sleep(1)
            
            else:
                total = int(argv.sec) + (60* int(argv.min)) + (3600 * int(argv.hour))
                if total == 0:
                    print("Cannot start a timer for 0 seconds")
                    sys.exit(0)
                else:
                    print(f"Starting a timer for {total} seconds")
                    for _ in range(1): sleep(total)
                    time_up()
        except KeyboardInterrupt:
            print('\nTimer canceled')
            sys.exit(0)
        except Exception as e:
            print(f"Error occurd: {e}")
            sys.exit(1)
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
