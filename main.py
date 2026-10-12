import threading

import mechanic, keyboard, timerclass


keyboard.initialize()
timer = timerclass.Clock()
i = 0


while True:
    timer.running(mechanic.WORKING, mechanic.WORK_STATE)
    timer.question()
    timer.running(mechanic.BREAKING, mechanic.BREAK_STATE)
    i += 1
    keyboard.wait_input()
    timer.question()
    keyboard.wait_input()


    if i == 3:
        timer.running(mechanic.WORKING, mechanic.WORK_STATE)
        timer.question()
        keyboard.wait_input()
        timer.running(mechanic.LONG_BREAKING, mechanic.LONG_BREAK_STATE)
        i = 0
        timer.question()
        keyboard.wait_input()


