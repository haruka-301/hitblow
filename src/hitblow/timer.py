import time


def start():
    return time.perf_counter()


def elapsed_since(started_at):
    return time.perf_counter() - started_at