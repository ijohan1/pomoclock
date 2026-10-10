from timer import Timer
# def _duration_in_minutes(minutes):
#     return minutes * _ONE_MINUTE_IN_SECONDS

_ONE_MINUTE_IN_SECONDS = 60
WORKING = 45 * _ONE_MINUTE_IN_SECONDS
# WORKING = _duration_in_minutes(45)
BREAKING = 5 * _ONE_MINUTE_IN_SECONDS
# BREAKING = _duration_in_minutes(5)
LONG_BREAKING = 10 * _ONE_MINUTE_IN_SECONDS
# LONG_BREAKING = _duration_in_minutes(10)
WORK_STATE = 'work'
BREAK_STATE = 'break'
LONG_BREAK_STATE = 'lunch'


class BaseMechanic:
    DURATION_IN_MINUTES = 0

    def __init__(self):
        self.timer = Timer()
        self.commands = Commands()

    def run(self):
        self.timer.run()

        while self.timer.minutes < self.DURATION_IN_MINUTES:
            self.commands.load()

            if self.commands.is_present():
                self._command_process()

    def _command_process(self):
        states = {
            'break': self.timer.pause,
            'stop': self.timer.stop
        }

        map(self.commands, lambda command: states[command]())


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

# ++++++++код код++++++++++++

