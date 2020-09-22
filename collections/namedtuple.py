from collections import namedtuple


Point = namedtuple('Point', 'x y z')  # second parameter is any iterables

p1 = Point(1, 2, 3)
print(p1)
print(list(p1))

print(p1.x)  # also p1[0]
print(p1.y)
print(p1.z)


print(p1._asdict)
print(p1._fields)
