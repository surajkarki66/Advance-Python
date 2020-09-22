# Basically there are two arguments
# 1) Formal argument => argument at the function definition
# 2) Actual argument => argument while calling the function

# Actual arguments has 4 types
# i) Position
# ii) Keyword
# iii) Default
# iv) Variable length


# Eg.
# Position => take care of position of all arguments
def person(name, age=0):
    print(name)
    print(age + 2)


person('Suraj', 21)
# person(21, 'Suraj') this throw an error

# Keywords => if you don't know sequence
person(age=20, name="Binish")

# Default
person('Saman')

# Variable length

# here we not always want to add 2 numbers, sometimes we want to add n numbers.
# here the no of arguments is not fixed.


def sum(*a):
    """
    Here *b means it accepts one or more than one value 
    from b
    """
    print(a)
    c = 0
    for i in a:
        c = c + i
    return c


sum(1, 2)
sum(1, 2, 3, 4)

print(sum(1, 3, 4, 5))

# another example


def mul(*x):
    m = 1
    for i in x:
        m *= i

    return m


print(mul(1, 2))
print(mul(1, 2, 3, 4))


# conventionally
def div(*args):
    return args


print(div(1, 2, "suraj", 5, 't'))
