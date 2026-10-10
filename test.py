import time
import threading
import termios
import sys


LFLAG_ATTRIBUTE_INDEX = 3

start = time.time()

is_running = True


def getch():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[LFLAG_ATTRIBUTE_INDEX] = new[LFLAG_ATTRIBUTE_INDEX] & ~termios.ICANON
    # new[LFLAG_ATTRIBUTE_INDEX] = new[LFLAG_ATTRIBUTE_INDEX] & ~termios.ECHO
    #
    # new[6][termios.VMIN] = 1
    # new[6][termios.VTIME] = 0
    try:
        # termios.tcsetattr(fd, termios.TCSAFLUSH, new)
        termios.tcsetattr(fd, termios.TCSADRAIN, new)
        read_character = sys.stdin.read(1)
    finally:
        # termios.tcsetattr(fd, termios.TCSAFLUSH, old)
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return read_character

def output():
    global is_running

    while is_running:
        now = int(time.time() - start)
        mins, secs = divmod(now, 60)
        print(f"\r | {mins:02d}:{secs:02d} | ", end='', flush=True)
        time.sleep(0.1)
    print()


def input_():
    global is_running

    while True:
        key = getch()
        # print('\r                                             ', end='', flush=True)
        if key == 'q':
            is_running = False
            break


threads = [
    threading.Thread(target=output, args=(), kwargs={}),
    threading.Thread(target=input_, args=(), kwargs={})
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
