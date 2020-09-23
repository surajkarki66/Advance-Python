# Decorators are higher order function that takes function as an argument and returns function
# with help of decorators we can add extra features in existing function without touching that function
# This is also called metaprogramming because a part of the program tries to modify another part of the program at compile time.

def division(a, b):
    return a / b


def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner


div1 = smart_div(division)
print(div1(1, 2))
