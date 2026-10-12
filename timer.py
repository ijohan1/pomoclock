import time


class Timer:
    ONE_MINUTE_IN_SECONDS = 60

    def __init__(self):
        self._total_second = 0

    def run(self):
        pass

    def pause(self):
        pass

    def stop(self):
        pass

    @property
    def seconds(self):
        return self._total_second % self.ONE_MINUTE_IN_SECONDS

    @property
    def minutes(self):
        return self._total_second // self.ONE_MINUTE_IN_SECONDS
