# filter method is higher order method that takes an function and iterables as parameter.
# And filter out the value from iterables and return filtered iterables

def add8(x):
    return x + 8

def isOdd(x):
    return x%2 != 0

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = list(filter(isOdd, a)) # here filter filter out the a list and give b list according to filter function.


print(b)

# Using  filter with map method
# one way
c = list(map(add8, b))
print(c)

# another
d = list(map(add8, filter(isOdd, a)))
print(d)

# Using lambda function

e = list(filter(lambda x: x % 2 != 0 , a))
print(e)


f = list(map(lambda x: x+8, filter(lambda x: x%2 !=0, a )))
print(f)