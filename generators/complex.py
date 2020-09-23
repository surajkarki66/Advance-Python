# if we try to run this it gives us memory error.
#x = [i**2 for i in range(100000000000)]


# OOp generator(advanced)


class Gen:
    def __init__(self, n):
        self.n = n
        self.last = 0

    def __next__(self):
        """
        next(g)
        """
        return self.next()

    def next(self):
        if self.last == self.n:
            raise StopIteration()
        rv = self.last ** 2
        self.last += 1
        return rv


g = Gen(10)
while True:
    try:
        print(next(g))
    except StopIteration:
        break
