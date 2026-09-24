#/usr/bin/env python3
import os, json, time, threading, sys
from datetime import datetime

import basevars, input_, output, json_



def main():
    global state, sessions
    counter = 0

    while running:
        if basevars.state == "work":
            timer.worktimer(sessions)
            counter += 1
            basevars.sessions += 1
            if counter %4 == 0: basevars.state = "lunch"
            else: basevars.state = "break"

        elif basevars.state == "break":
            timer.breaktimer(sessions)
            basevars.state = "work"

        elif basevars.state == "lunch":
            timer.lunchtimer(sessions)
            basevars.state = "work"


