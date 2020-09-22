li = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def func(x):
    return x**x

# to apply above function to every value of list above.

# One way
li2 = []
for i in li:
    result = func(i)
    li2.append(result)

print(li2)

# Best way is to use map method

li3 = map(func, li)
print(list(li3))


li4 = map(lambda x : x**x, li)
print(list(li4))


