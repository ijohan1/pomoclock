import os, threading

def inputs():
    while True:
        cmd = input()
        if cmd == "":
            os.system("read -n1")
        elif cmd == "q":
            break
       

input_thread = threading.Thread(target=inputs, daemon=True)
output_thread = threading.Thread(target=inputs, daemon=True)

def wait_input():
    input_thread.wait()


def initialize():
    input_thread.start()