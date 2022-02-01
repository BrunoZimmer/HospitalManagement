
class Connection:
    """ A sample Beacons class"""
#this class is not the beacons itselfs, but the mobiles connected to then
    # ID is the id of the beacons to connect
    # room
	# Distance is the distance of the beacon to the mobile connected
	# Patient of the person connected to the beacon
    def __init__(self, id, room, distance, namePatient):
        self.id = id
        self.room = room
        self.distance = distance
        self.namePatient = namePatient

    @property
    def namePatientAndRoom(self):
        return '{} {}'.format(self.namePatient, self.room)


    def __repr(self):
        return "Beacon('{}', '{}', '{}')".format(self.id, self.distance, self.namePatient)