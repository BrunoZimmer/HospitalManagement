
class Beacon:
    """ A sample Beacons class"""

        # id text,
        # bedsTotal integer,
        # bedsFree integer,
        # room text
    def __init__(self, id, bedsTotal, bedsFree, room):
        self.id = id
        self.bedsTotal = bedsTotal
        self.bedsFree = bedsFree
        self.room = room

    @property
    def room(self):
        return '{}'.format(self.room)

    @property
    def freeBeds(self):
        return '{}'.format(self.bedsFree)

    def __repr(self):
        return "Beacon('{}', '{}', '{}')".format(self.id, self.distance, self.user)