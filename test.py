import time
import threading
from submission import *


def test():
    start_job('start_job')
    for i in range(10):
        # Simulate some time consuming task
        time.sleep(2)
        log_metric('test_1', 2)
        print(threading.enumerate())


if __name__ == '__main__':
    test()