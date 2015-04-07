# MethodType is the type class for the methods of user-defined class instances.
# FunctionType is the type class for user-defined functions.
# LambdaType is the type class for functions created by lambda expressions.

# Abstract:
# When dynamically adding a method to a class instance the "self" argument is
# not automatically passed as the class instance


# A method(MethodType): has an attribute called __self__ which is equal to an
# instance of to its parent class. It also has an attribute called __func__
# which is equal to a reference to the callable function.

# It seems that a method is just a callable class, that class being MethodType
# player.dribble is actually not a function reference but
# a class instance(MethodType)

# To dynamically add a new method to an instance of a class, you must set the
# method name to an instance of MethodType passing a function reference and
# the parent class instance which will be set to __func__ and __self__
# respectively

# class MethodType:
#     def __init__(self, function, instance_parent):
#         self.__func__ = function
#         self.__self__ = instance_parent


import types


class Player:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.dominant_foot = kwargs.get('dominant_foot')

    def dribble(self):
        speed = 0
        print('dribbling')

player = Player(name='Messi', dominant_foot='Left')


def kick(self):
    print(self)


print(type(player))
print(type(player.dribble))
print(type(kick))

# dir() gets a list of all the attributes of a class instance
print(dir(player.dribble))

player.kick = types.MethodType(kick, player)

print(player.kick)