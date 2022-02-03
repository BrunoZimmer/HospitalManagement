import math
from queue import PriorityQueue


def CreatePatient(list):
    pat = Patient(list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7],list[8],list[9])
    
    return pat

class Patient:
    """ A sample Employee class"""

#   Name
#   id
# 	Arrival time (arrival in the reception)
# 	Depart time (depart from reception to the room)
# 	Disease
# 	Specifications
    def __init__(self, id, name, priority, arrival, depart, stayingTime, state, type, disease, specs):
        self.id = id
        self.name = name
        self.priority = priority
        self.arrival = arrival
        self.depart = depart
        self.stayingTime = stayingTime
        self.state = state
        self.type = type
        self.disease = disease
        self.specs = specs

    @property
    def fullname(self):
        return '{}'.format(self.name)

    @property
    def waitingTime(self):
        return (self.depart.timestamp() - self.arrival.timestamp())

    @property
    def diseaseSpec(self):
        return '{} {}'.format(self.disease, self.specs)
    
    @property
    def waitingPriority(self):
        return math.exp(self.waitingTime*0.000185-7)
    
    @property
    def typePriority(self):
        priorityBytype = {
            "Regular": 0.1,
            "Emergency": 0.2,
            "Covid-19": 0.3
        }
        return priorityBytype.get(self.type)
    
    @property
    def makePriority(self):
        return self.waitingPriority +self.typePriority
    
    def __repr(self):
        return "Patient('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            self.id, self.name, self.priority, self.arrival, self.depart, self.stayingTime, self.type, self.disease, self.specs
            )