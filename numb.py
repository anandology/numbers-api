"""Numbers library.
"""

def fibs(a, b, n):
    for i in range(n):
        yield a
        a, b = b, a+b

def product(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result