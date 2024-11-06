import time
from submission import *


def main():
    start_job('start_job')
    log_job('log_job', 0.75)
    log_metric('log_metric', 23)
    time.sleep(5)
    log_metric('log_metric', 34)
    time.sleep(5)
    log_metric('log_metric', 45)
    time.sleep(5)
    log_metric('log_metric', 56)
    time.sleep(5)
    log_metric('log_metric', 67)


if __name__ == "__main__":
    main()
