# One important thing is the wrapper function inside the decorator must have same parameters as of function that we want to decorate

def func(f):
    def wrapper(*args, **kwargs):
        print("Started")
        result = f(*args, **kwargs)
        print("Finished")
        return result

    return wrapper


@func
def func2(x):
    return x


@func
def func3():
    print("Im func3")


print(func2(4))
