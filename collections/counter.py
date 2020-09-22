from collections import Counter

# Container
# => In python container stores the multiple python objects.
# => This module implements specialized container datatypes providing alternatives to Python's general purpose built-in containers, dict, list, set, and tuple.
# => eg of containers are
# list
# tuple (immutable)
# set
# dictionary

# Types
# 1) Counter
# 2) dequeue
# 3) namedTuple
# 4) orderedDict
# 5) defaultdict

c = Counter('suraj')  # it takes container as an argument
print(c)
print(list(c.elements()))
print(c.most_common(2))
print("")


c = Counter(['a', 'a', 'b', 'c', 'd'])
print(c)
print(list(c.elements()))
print(c.most_common(2))
print("")

c = Counter({"a": 1, "b": 2})
print(c)
print(c['b'])
print(list(c.elements()))
print(c.most_common(2))
print("")

c = Counter(cats=4, dogs=7)
print(c)
print(c['dogs'])
print(list(c.elements()))
print(c.most_common(2))
print("")


d = Counter(a=4, b=2, c=0, d=-2)
e = Counter(['a', 'b', 'b', 'c'])

print(d+e)
print(d-e)
