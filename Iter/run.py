class Iterable:

    class Iterator:
        def __init__(self, items):
            self.items = items
            self.index = -1
            self.length = len(self.items)

        def __next__(self):
            self.index += 1

            if not self.index < self.length:
                raise StopIteration

            return self.items[self.index]

    def __init__(self):
        self.items = [1, 2, 3]

    def __iter__(self):
        return Iterable.Iterator(self.items)


# Create an Iterator to print out the Fibonacci

class Fibonacci:

    class Iterator:
        def __init__(self, limit):
            self.limit = limit
            self.count = 0
            self.a = 0
            self.b = 1

        def __next__(self):
            self.count += 1

            if not self.count < self.limit:
                raise StopIteration

            self.b += self.a
            self.a = self.b - self.a

            return self.b

    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        return Fibonacci.Iterator(self.limit)


fibonacci = Fibonacci(100)

for value in fibonacci:
    print(value)