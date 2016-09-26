# Abstract:
# An object is created for the class name, this object is of type `type`
# Using a metaclass allows you to change the type of that object

class Man:
    pass

print(type(Man))
# <class 'type'>

class Human(type):
    def __new__(cls, *args, **kwargs):
        print('creating Human object')
        return super().__new__(cls, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        print('calling Human object')

class Woman(metaclass=Human):
    pass

print(type(Woman))
# <class '__main__.Human'>
