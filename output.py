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
