import math

class elevator:

    def __init__(self, speed = 0, close = 0, open = 0, start = 0, stop = 0) -> None:
        self.speed = speed
        self.closeTime = close
        self.openTime = open
        self.startTime = start
        self.stopTime = stop

        self.state = 0 #0 -resting, -1 -gowing down, 1 -going up
        self.flour = 0

    def __str__(self):
        s = "speed: " + str(self.speed) + ", "
        s += "closeTime: " + str(self.closeTime) + ", "
        s += "openTime: " + str(self.openTime) + ", "
        s += "startTime: " + str(self.startTime) + ", "
        s += "closeTime: " + str(self.closeTime) + ", "
        s += "state: " + str(self.state) + ", "
        s += "flour: " + str(self.flour)
        return s

        self.state = 0 #0 -resting, -1 -going down, 1 -going up
        self.flour = 0

    def Time(self, source, dest):
        return ((math.fabs(source - dest)) / self.speed) + self.openTime + self.closeTime + self.startTime + self.stopTime