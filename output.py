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

def ascii(state):
    if state == "work":
        return floppy
    else: return cacti



def render(paused, state, seconds, sessions):
    clear()
    print(ascii(state))
    mins, secs = divmod(seconds, 60)
    line = (f" | {state} |  {mins:02d}:{secs:02d} | "f"сесій: {sessions} |")
    if paused:
        print(line + " ⏸ ") #, end = "\r"
    else: print(line) #, end = "\r"



def showstats():
    clear()
    hours = totalseconds // 3600
    mins = (totalseconds % 3600) // 60
    secs = totalseconds % 60
    print(f"роботу завершено.\n відроблених помодоро сесій: {sessions}.\n було відпрацьовано {hours}г. {mins}хв. {secs}с.")

