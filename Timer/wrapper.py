import functools
import time


def functimer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed_time = end - start
        print(f"Elapsed time: {elapsed_time:.04f} seconds")
        return value
    return wrapper_timer
