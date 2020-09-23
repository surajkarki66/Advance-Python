import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func(*args, **kwargs)
        elapsed = time.time() - start
        print("Time: ", elapsed)
        return rv

    return wrapper


@timer
def test():
    for _ in range(1000000):
        pass


test()
