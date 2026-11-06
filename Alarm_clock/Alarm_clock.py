
from playsound3 import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\03[H"

def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed +=1


        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        
        print(f"\rAlarm will sound in: {minutes_left:02d}:{seconds_left:02d}", end="", flush=True)

    playsound("Alarm_clock/Alarm-Fast-High-Pitch-A1-www.fesliyanstudios.com.mp3")

minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)