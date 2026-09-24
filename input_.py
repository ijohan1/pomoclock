def inputs():
    global paused, waiting, running, sessions
    while True:
        cmd = input()
        if cmd == "q":
            running = waiting = False
            break

        if waiting: waiting =  False
        else:
            paused = not paused
            if not paused: clear()
