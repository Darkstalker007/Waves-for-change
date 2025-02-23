import random

class drive:
    id= None
    distination= None
    duration= None
    time= None
    active= None

    def __init__(self,destination,duration,time,active):
        self.id=random.randint(1,1000)
        self.destination=destination
        self.duration=duration
        self.time=time
        self.active=active

    def __getattribute__(self, id):
        return self.id