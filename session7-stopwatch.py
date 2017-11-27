from time import time,sleep

x = time()
sleep(2)
y = time()
print(y- x)


class StopWatch:
    def __init__(self):
        self.__start_time = time ()
        self.__end_time = time()

    def getStartTime(self):
        return self.__start_time
    def getEndTime(self):
        return self.__end_time

    def start(selfself):
        self.__start_time = time()

    def stop(self):
        self.__end_time = time()

    def get_elapsed_time(self):
        return self.__end_time - self.__start_time

sw = StopWatch()
sw.start
for i in range (10000):
   x= i/10
sw.stop()
print(sw.get_elapsed_time())

