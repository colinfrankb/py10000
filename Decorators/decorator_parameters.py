# A Decorator that accepts arguments will be initialized and have its __call__ method called to which the
# function it is wrapping will be passed, a function reference that calls the wrapped function should be returned
# NOTE: a function reference is returned

# A Decorator that does not accept arguments will be initialized and returned not a function reference,
# the wrapped function must be called inside the __call__
# NOTE: a callable class instance is returned

class DecoratorWithArgs:
    def __init__(self, route):
        print("initialized")
        print(route)

    def __call__(self, f):
        print("decorator called")
        print(f)
        def wrapper():
            print("wrapped action")
            f()
        return wrapper


class DecoratorWithOutArgs:
    def __init__(self, f):
        print("initialized")
        self.f = f
        print(self.f)

    def __call__(self):
        print("decorator called")
        self.f()


@DecoratorWithArgs("/index")
def action_a():
    print("action a called")


@DecoratorWithOutArgs
def action_b():
    print("action b called")