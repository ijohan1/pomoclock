import time

import mechanic



class Clock():
    def __init__(self):
        self.runs = 'Rybka'
        self.waiting = False
        self.paused = False
        self.state = None

    def running(self, duration, state):
        start = time.time()
        elapsed = 0
        last_paused = None
        seconds = duration
        total_seconds = 0


        while seconds > 0:
            if self.paused:
                if last_paused is None:
                    last_paused = time.time()
                time.sleep(0.1)
                continue


            if last_paused is not None:
                elapsed += time.time() - last_paused
                last_paused = None

            time_passed = start + elapsed
            remained = int(time.time() - time_passed)
            seconds = duration - remained
            
            
            time.sleep(0.2)
            total_seconds += (duration - seconds)
            print("done.")
            self.waiting = True
            while self.waiting: 
                time.sleep(0.1)


            mins, secs = divmod(duration, 60)
            line = (f" | {state} |  {mins:02d}:{secs:02d} |")
            if self.paused:
                print(line + " ⏸ ") #, end = "\r"
            else: print(line) #, end = "\r"
    


    def question(self):
        next = input("\nnext?")
        if next == True:
            os.system("clear")
            pass
        elif next == 'q':
            print("\nkthxbye")
            return


#    def output(self):
