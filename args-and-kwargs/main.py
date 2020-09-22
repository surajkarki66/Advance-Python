# *args and **kwargs

def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)


foo('hello')
foo('hello', 1, 2, 3, 4)
foo('hello', 1, 2, 3, 4, key1='value', key2='400')


# apps

'''
def foo(x, *args, **kwargs):
    kwargs['name'] = 'Alice'
    new_args = args + ('extra',)
    bar(x, *new_args, **kwargs)
'''

# it is also used in subclassing


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


class AlwaysBlueCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 'blue'


a = AlwaysBlueCar("Red", 120)
print(a.color)
