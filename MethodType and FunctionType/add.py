import types


class Player:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.dominant_foot = kwargs.get('dominant_foot')

    def dribble(self):
        speed = 0
        print('dribbling')


Player.whatsmyname = lambda self: print(self.name)

player = Player(name='Messi')
# player.whatsmyname = types.MethodType(lambda self: print(self.name), Player)

player.whatsmyname()
