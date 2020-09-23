def func(func):
    # THis is my decorator
    def wrapper():
        print("Started")
        func()
        print("End")

    return wrapper


def func2():
    print("I am func2")


func2 = func(func2)
print(func2)
func2()


# The above approach is not good .
# The best practice for decorator is
def func_decorator(func):
    # THis is my decorator
    def wrapper():
        print("Started")
        func()
        print("End")

    return wrapper


@func_decorator
def func3():
    print("I am func3")


func3()
