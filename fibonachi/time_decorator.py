import time

def time_decorator(func):

    def wrapper(*args):
        start_time = time.time()
        res = func(*args)
        print("--- %s seconds ---" % (time.time() - start_time))

    return wrapper
