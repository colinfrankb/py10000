import types


class BandMeta(type):
    def __prepare__(self):
        super().__prepare__()


class Band(object):
    def __init__(self, name=''):
        self.name = name

    def __getitem__(self, item):
        return self.__dict__[item]


band = Band(name='KOL')

# print(type(band).__getitem__(band, 'name'))
print(band['name'])

club_type = type('RockBand', (Band,), {'genre': 'Rock Music'})

rock_band = club_type()

print(rock_band.genre)

