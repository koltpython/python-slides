def fibonacci_series(limit):
    """Returns a list of the Fibonacci series up to limit."""
    fib_list = []
    first = 0
    second = 1
    while first < limit:
        fib_list.append(first)
        first, second = second, first + second
    return fib_list

print(fibonacci_series)