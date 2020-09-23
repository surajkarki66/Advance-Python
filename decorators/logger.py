def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(
        original_function.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return original_function(*args, **kwargs)

    return wrapper


def my_timer(original_function):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print("{} ran in : {} sec".format(original_function.__name__, t2))
        return result

    return wrapper


@my_logger
def display():
    print('display function ran')


@my_timer
def display_info(name, age):
    print('Display info ran with arguments ({}, {})'.format(name, age))


#d = decorator_class(display)
# print(d())

display()
display_info(name="Suraj", age=20)
