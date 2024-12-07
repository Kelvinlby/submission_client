import time
import threading

from submission import *


def test():
    time.sleep(5)
    start_job('test')
    for i in range(6):
        # Simulate some time consuming task
        time.sleep(1)
        log_metric('test_2', 2)
        log_metric('test_3', 3)
        log_metric('test_4', 4)
        log_job('test', i*0.2)
        log_job('test_1', i*0.3)
        print(threading.enumerate())
    end_job('test')
    end_job('test_1')


if __name__ == '__main__':
    test()