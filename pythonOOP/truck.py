class Vehicle:
    def __init__(self):
        self.velocity = 50
        
    def getVelocity():
        return self.velocity

class Machine:
    def __init__(self):
        self._distanceTravelled = 100
    def getDistance():
        return self.distanceTravelled

class Truck(Vehicle, Machine):
    def __init__(self, velocity,time):
        Vehicle.__init__(self)
        Machine.__init__(self)
        self.velocity = velocity
        self.time = time
        
    def getVelocity():
        return self.distanceTravelled/self.time
        
    def getDistance():
        return self.velocity * time