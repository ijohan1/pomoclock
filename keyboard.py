import os, threading

def inputs():
    while True:
        cmd = input()
        if cmd == "":
            os.system("read -n1")
        elif cmd == "q":
            break
       

thread = threading.Thread(target=inputs, daemon=True)
