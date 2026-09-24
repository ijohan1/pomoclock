import os, json, time, threading, sys
from datetime import datetime

import basevars

def beep(): #change for sound
    os.system('canberra-gtk-play -i complete')


def basetimer(duration, state, sessions):
#    global paused, waiting, totalseconds, running
    start = time.time()
    elapsed = 0
    lastpaused = None
    seconds = duration

#=======пауза і рух===========
    while seconds > 0 and running:
        if paused:
            if lastpaused is None: lastpaused = time.time()
            render(paused, state, seconds, sessions)
            time.sleep(0.1)
            continue

        if lastpaused is not None:
            elapsed += time.time() - lastpaused
            lastpaused = None

        elapsed_ = int(time.time() - start - elapsed)
        seconds = duration - elapsed_

        render(paused, state, seconds, sessions)
        time.sleep(0.2)
#=======================
    global totalseconds
    totalseconds += (duration - seconds)
    beep()
    print("час вийшов. далі? (enter)")
    waiting = True
    while waiting and running: time.sleep(0.1)

def worktimer(sessions):
    basetimer(work, "work", sessions)

def breaktimer(sessions):
    basetimer(breakk, "break", sessions)

def lunchtimer(sessions):
    basetimer(lunch, "lunch", sessions)

