import time

def start_timer():
    return time.time()

def elapsed_time(start):
    return time.time() - start