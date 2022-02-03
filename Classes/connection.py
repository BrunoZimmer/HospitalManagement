
def CreateConnection(list):
    connec = Connection(list[0],list[1],list[2],list[3])
    
    return connec

class Connection:
    """ A sample Beacons class"""
#this class is not the beacons itselfs, but the mobiles connected to then
# con_ID TEXT PRIMARY KEY,
# beac_ID TEXT,
# pat_ID TEXT,
# distance FLOAT
    def __init__(self, con_ID, beac_ID, pat_ID, distance):
        self.con_ID = con_ID
        self.beac_ID = beac_ID
        self.pat_ID = pat_ID
        self.distance = distance

    @property
    def namePatientAndRoom(self):
        return '{} {}'.format(self.distance, self.beac_ID)

    def __repr(self):
        return "Beacon('{}', '{}', '{}', '{}')".format(self.con_ID, self.beac_ID, self.pat_ID, self.distance)