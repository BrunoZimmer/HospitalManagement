
class Patient:
    """ A sample Employee class"""

#   Name
#   id
# 	Arrival time (arrival in the reception)
# 	Depart time (depart from reception to the room)
# 	Disease
# 	Specifications
    def __init__(self, name, id, arrival, depart, disease, specs):
        self.id = id
        self.name = name
        self.arrival = arrival
        self.depart = depart
        self.disease = disease
        self.specs = specs

    @property
    def fullname(self):
        return '{}'.format(self.name)

    @property
    def waitingTime(self):
        return (self.depart - self.arrival)

    @property
    def diseaseSpec(self):
        return '{} {}'.format(self.disease, self.specs)

    
    def __repr(self):
        return "Patient('{}', '{}', '{}', '{}', '{}', '{}')".format(
            self.id, self.name, self.arrival, self.depart, self.disease, self.specs
            )