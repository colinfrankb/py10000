from collections import OrderedDict

class _OrderedDictMaker(object):
    def __getitem__(self, keys):
        print(keys)
        assert isinstance(keys, tuple)
        assert all(isinstance(key, slice) for key in keys)

        return OrderedDict([(k.start, k.stop) for k in keys])

ordereddict = _OrderedDictMaker()

# When __getitem__ is called e.g 'abcd'[0:1] python interpreter will
# generate slice instances for arguments that match this syntax 'key': 'value'

menu = ordereddict[
    'about': 'about'
]

# When multiple arguments are passed it will initialise a tuple of the
# arguments regardless of the argument types

menu = ordereddict[
    'about': 'about', 'another string'
]

# The python interpreter will only generate slice instances when __getitem__
# is called

# Proof that other __getitem__ implementations follow the same rules above,
# but handle the arguments differently, since it doesn't throw a syntax error

# >>> "abcd"[0:1,0:2]

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: string indices must be integers


# >>> {'name': 'colin'}['name':'test']

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'slice'


# >>> sl = slice('name')
# >>> dic = {'name': 'colin'}
# >>> dic[sl]

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unhashable type: 'slice'