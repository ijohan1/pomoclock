def working():
    duration = 45 * 60
    return duration 


def breaking():
    duration = 5  * 60
    return duration 


def longBreaking():
    duration = 10  * 60
    return duration 



def workState():
    state = 'work'
    return state


def breakState():
    state = 'break'
    return state

def longBreakState():
    state = 'lunch'
    return state




#def working():
#    print("work")
#    timer.countdown(modes.work())
#    os.system('clear')
#
#def breaking():
#    print("break")
#    timer.countdown(modes.smallBreak())
#    os.system('clear')
#
#def longBreaking():
#        print("longbreak")
#        timer.countdown(modes.longBreak())
#        os.system('clear')

#
#def question():
#    next = input("\nnext?")
#    if next == True:
#        os.system("clear")
#        pass
#    elif next == 'q':
#        print("\nkthxbye")
#        return
