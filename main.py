#/usr/bin/env python3


import os, json, time, threading, sys
from datetime import datetime


def main():
    global state, sessions
    counter = 0

    while running:
        if state == "work":
            worktimer(sessions)
            counter += 1
            sessions += 1
            if counter %4 == 0: state = "lunch"
            else: state = "break"

        elif state == "break":
            breaktimer(sessions)
            state = "work"

        elif state == "lunch":
            lunchtimer(sessions)
            state = "work"


