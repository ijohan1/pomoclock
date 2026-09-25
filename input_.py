import basevars

def inputs():
    while True:
        cmd = input()
        if cmd == "q":
            basevars.running = waiting = False
            break

        if waiting: waiting =  False
        else:
            basevars.paused = not pbasevars.paused
            if not basevars.paused: clear()
