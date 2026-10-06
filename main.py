import threading

import mechanic, keyboard, timerclass


keyboard.thread.start()
timer = timerclass.Clock()
i = 0


while True:
    timer.running(mechanic.working(), mechanic.workState())
    timer.question()
    timer.running(mechanic.breaking(), mechanic.breakState())
    i += 1
    keyboard.thread.wait()
    timer.question()
    keyboard.thread.wait()


    if i == 3:
        timer.running(mechanic.working(), mechanic.workState())
        timer.question()
        keyboard.thread.wait()
        timer.running(mechanic.longBreaking(), mechanic.longBreakState())
        i = 0
        timer.question()
        keyboard.thread.wait()


