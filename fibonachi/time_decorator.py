import time
def time_decorator(func):
    def wrapper():
        start_time =time.time()
        func()
        print("--- %s seconds ---" % (time.time() - start_time))
