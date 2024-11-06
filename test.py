import time

from submission import log_metric, start_job, end_job


def main():
    for i in range (10):
        start_job('train')
        log_metric('loss', 0.5+i)
        i += 1
        end_job('train')
        time.sleep(5)

if __name__ == "__main__":
    main()