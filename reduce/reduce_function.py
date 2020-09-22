import functools
import operator

li = [1, 3, 5, 6, 2]

s = functools.reduce(lambda a, b: a + b, li)
print(s)

m = functools.reduce(lambda a, b: a * b, li)
print(m)


# Another
d = functools.reduce(operator.mul, li)
print(d)

print(operator.mul)