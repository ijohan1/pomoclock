import threading

import mechanic, keys


keys.thread.start()

i = 0

while True:
    mechanic.working()
    mechanic.question()
    mechanic.breaking()
    i += 1
    keys.thread.wait()
    mechanic.question()
    keys.thread.wait()

    if i == 3:
        mechanic.working()
        mechanic.question()
        keys.thread.wait()
        mechanic.longBreaking()
        i = 0
        mechanic.question()
        keys.thread.wait()
