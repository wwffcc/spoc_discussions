# coding=utf-8
import threading
import random
import time

s = mutexa = mutexb = 1
sa = sb = 0
box = random.choice([0, 1])


class processAdmin(threading.Thread):

    def __init__(self, threadName, semaphore):
        threading.Thread.__init__(self, name=threadName)
        self.sleepTime = random.randrange(1, 6)
        self.threadSemaphore = semaphore

    def run(self):
        self.threadSemaphore.acquire()
        # critical zone
        self.threadSemaphore.release()
