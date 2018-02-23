import time
from subprocess import call
mintt=input("How many seconds you want to time?:")
timer=int(mintt)
while (timer != 0 ):
    timer=timer-1
    time.sleep(1)
    print(timer)
    if (timer == 0 ):
	call (["afplay", "Airhorn.wav"])

