import time

from submission import  log_metric

def main():
    for i in range (10):
        log_metric('loss', 0.5+i)
        i += 1
        time.sleep(0.5)

if __name__ == "__main__":
    main()