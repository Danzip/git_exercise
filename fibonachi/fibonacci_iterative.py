import fibonachi_recursive
import time_decorator


def fibonachi_iterative(n):
    for i in range(n):
        yield i

@time_decorator.time_decorator
def nexter(n):
    g = fibonachi_iterative(10)
    for e in g:
        print(fibonachi_recursive.fibonachi_recursive(e))

nexter(30)