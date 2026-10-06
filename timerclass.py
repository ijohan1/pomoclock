import time

import mechanic



class Clock():
    def __init__(self):
        self.runs = self.running
        self.waiting = False
        self.paused = False
        self.state = None

    def running(self, duration, state):
        start = time.time()
        elapsed = 0
        lastPaused = None
        seconds = duration
        totalSeconds = 0


        while seconds > 0 and self.running:
            if self.paused:
                if lastPaused is None:
                    lastPaused = time.time()
                time.sleep(0.1)
                continue


            if lastPaused is not None:
                elapsed += time.time() - lastPaused
                lastPaused = None


            remained = int(time.time() - start - elapsed)
            seconds = duration - remained
            
            
            time.sleep(0.2)
            totalSeconds += (duration - seconds)
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
