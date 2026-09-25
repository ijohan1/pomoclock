import os, time
from datetime import datetime

import basevars

def beep(): #change for sound
    os.system('canberra-gtk-play -i complete')


def basetimer(duration, basevars.state, basevars.sessions):
#    global paused, waiting, totalseconds, running
    start = time.time()
    elapsed = 0
    lastpaused = None
    seconds = duration

#=======пауза і рух===========
    while seconds > 0 and running:
        if paused:
            if lastpaused is None: lastpaused = time.time()
            render(basevars.paused, basevars.state, seconds, basevars.sessions)
            time.sleep(0.1)
            continue

        if lastpaused is not None:
            elapsed += time.time() - lastpaused
            lastpaused = None

        elapsed_ = int(time.time() - start - elapsed)
        seconds = duration - elapsed_

        render(basevars.paused, basevars.state, seconds, basevars.sessions)
        time.sleep(0.2)
#=======================
    basevars.totalseconds += (duration - seconds)
    beep()
    print("час вийшов. далі? (enter)")
    basevars.waiting = True
    while basevars.waiting and basevars.running: time.sleep(0.1)

def worktimer(sessions):
    basetimer(basevars.work, "work", basevars.sessions)

def breaktimer(sessions):
    basetimer(basevars.breakk, "break", basevars.sessions)

def lunchtimer(sessions):
    basetimer(basevars.lunch, "lunch", basevars.sessions)
    

