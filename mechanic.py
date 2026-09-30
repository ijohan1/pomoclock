import os, threading

import timer, modes, keys



def working():
    print("work")
    timer.countdown(modes.work())
    os.system('clear')

def breaking():
    print("break")
    timer.countdown(modes.smallBreak())
    os.system('clear')

def longBreaking():
        print("longbreak")
        timer.countdown(modes.longBreak())
        os.system('clear')


def question():
    next = input("\nnext?")
    if next == True:
        os.system("clear")
        pass
    elif next == 'q':
        print("\nkthxbye")
        return


