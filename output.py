import os

import basevars



floppy = (""" _.........._
| |        | |
| |        | |
| |        | |
| |________| |
|   ______   |
|  |    | |  |
|__|____|_|___""")

cacti = ("""           .:'
         __ :'__
      .'`__`-'__``.
     :__________.-'
     :_________:
      :_________`-;
       `.__.-.__.'""" )

def clear(): os.system('cls' if os.name=='nt' else 'clear')

def ascii(basevars.state):
    if basevars.state == "work":
        return floppy
    else: return cacti



def render(basevars.paused, basevars.state, basevars.seconds, basevars.sessions):
    clear()
    print(ascii(basevars.state))
    mins, secs = divmod(basevars.seconds, 60)
    line = (f" | {basevars.state} |  {mins:02d}:{secs:02d} | "f"сесій: {basevars.sessions} |")
    if basevars.paused:
        print(line + " ⏸ ") #, end = "\r"
    else: print(line) #, end = "\r"



def showstats():
    clear()
    hours = totalbasevars.seconds // 3600
    mins = (totalbasevars.seconds % 3600) // 60
    secs = totalbasevars.seconds % 60
    print(f"роботу завершено.\n відроблених помодоро сесій: {basevars.sessions}.\n було відпрацьовано {hours}г. {mins}хв. {secs}с.")

