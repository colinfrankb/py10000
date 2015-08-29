#!/usr/bin/env python

# using the built-in iter and a sentinel value method to print out the Fibonacci

class Fibonacci:

    def __init__(self):
            self.a = 0
            self.b = 1

    def __call__(self):
        self.b += self.a
        self.a = self.b - self.a

        return self.b

for value in iter(Fibonacci(), 987):
    print(value)
