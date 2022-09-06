class Clock:
    def __init__(self, time = 0):
        self.__time = time

    def set_time(self, tm):
        if self.check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time

    def check_time(self, tm):
        return (type(tm) is int) & (0 <= tm < 100000)

clock = Clock()
clock.set_time(4530)

