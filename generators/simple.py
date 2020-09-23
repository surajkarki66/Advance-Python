import sys

# simple gen


def gen(n):
    for i in range(n):
        yield i**2


g = gen(10000)
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))

x = [i ** 2 for i in range(10000)]

# memory allocation
print(sys.getsizeof(x))
print(sys.getsizeof(g))
