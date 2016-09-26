# Abstract:
# `type()` an object of type `type`
# `type` is an object of type `type`
# class names (class declarations) become objects of type `type`

# any instance/object when called will go to __call__

# All of the below creates an object of type `type`

class Man:
    pass

Mammal = type('Mammal', (), {})

class NewType(type):

    def __new__(mcs, name, bases, attrs):
        print('A type object is returned')
        return super().__new__(mcs, name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        print('A Human object is created.')
        return super().__call__(*args, **kwargs)

print(type(Mammal))
# <class 'type'>

print(type(NewType))
# <class 'type'>

print(type(Man))
# <class 'type'>


# The name NewType is an instance of `type`, therefore when called it will call
# type.__call__, which will call __new__ and __init__ to create a
# new object of type NewType

# NewType.__new__ will receive the arguments to type.__call__
Human = NewType('Human', (), {})

print(type(Human))
# <class '__main__.NewType'>

# Calling the type object (NewType inherits from type) calls __call__,
# which then calls __new__ and __init__ to create a new object
human = Human()


# Additional Example
class Woman:
    def __new__(cls, *args, **kwargs):
        pass

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        pass

# When you create an instance/object of Woman, you are just calling the type
# object `Woman` i.e type.__call__, with arguments that will
# be passed to __new__

new_object = Woman()

# Which then create a new object of type `Woman` by calling
# __new__ then __init__ of the `Woman` class
