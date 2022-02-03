
def CreateBeacon(list):
    beac = Beacon(list[0],list[1],list[2],list[3],list[4],list[5],list[6])
    
    return beac

class Beacon:
    """ A sample Beacon class"""

        # id text,
        # bedsTotal integer,
        # bedsFree integer,
        # price INTEGER,
        # reservation INTEGER,
        # room text
    def __init__(self, id, bedsTotal, bedsFree, price, reservation, room, specs):
        self.id = id
        self.bedsTotal = bedsTotal
        self.bedsFree = bedsFree
        self.price = price
        self.reservation = reservation
        self.room = room
        self.specs = specs

    @property
    def showRoom(self):
        return '{}'.format(self.room)

    @property
    def freeBeds(self):
        return '{}'.format(self.bedsFree)

    def __repr(self):
        return "Beacon('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
                self.id, self.bedsTotal, self.bedsFree, self.price, self.reservation, self.room, self.specs
            )