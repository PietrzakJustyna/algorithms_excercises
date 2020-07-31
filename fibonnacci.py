def fibonacci_iter(n):
    if n == 0:
        return 0
    a = b = 1
    for i in range(n-1):
        a, b = b, a + b
    return a


print(fibonacci_iter(10))


def fibonacci_recur(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fibonacci_recur(n-1) + fibonacci_recur(n-2)
        return result


print(fibonacci_recur(10))


