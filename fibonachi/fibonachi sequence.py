import fibonachi_recursive
import time_decorator

@time_decorator.time_decorator
def fibonachi_sequence(n):
    for i in range (n):
        print(fibonachi_recursive.fibonachi_recursive(i))

fibonachi_sequence(30)