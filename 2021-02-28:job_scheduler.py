import time
import threading


def job_scheduler(f, n):
    def delayed_f():
        time.sleep(1e-3 * n)
        f()
    threading.Thread(target=delayed_f)


job_scheduler(lambda: print("hello"), 1000)
job_scheduler(lambda: print("hi"), 500)
