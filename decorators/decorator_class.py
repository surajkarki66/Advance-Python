class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("Call method executed this before {}".format(
            self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@decorator_class
def display():
    print('display function ran')


@decorator_class
def display_info(name, age):
    print('Display info ran with arguments ({}, {})'.format(name, age))


#d = decorator_class(display)
# print(d())

display()
display_info(name="Suraj", age=20)
