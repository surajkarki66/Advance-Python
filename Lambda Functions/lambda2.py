def func(x):
    return x+5

func2 = lambda x: x+5
print(func(5))
print(func2(5))



cube_func = lambda x : x**3

a = [1, 2, 3, 4]

for i in a:
    print(cube_func(i))


def square(x):
    cube = cube_func(x)
    return int(cube / x)

print(square(5))