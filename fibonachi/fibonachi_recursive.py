
def fibonachi_recursive(n):
    if (n <= 1):
        return n

    return (fibonachi_recursive(n-1)) + fibonachi_recursive(n-2)

