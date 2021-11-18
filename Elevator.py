import math


class Elevator:

    def __init__(self, speed=0, close=0, open=0, start=0, stop=0) -> None:
        self.speed = speed
        self.closeTime = close
        self.openTime = open
        self.startTime = start
        self.stopTime = stop

        self.state = 0  # 0 - resting, -1 - going down, 1 - going up
        self.floor = 0
        self.inMotion = False

    def __str__(self):
        s = "speed: " + str(self.speed) + ", "
        s += "closeTime: " + str(self.closeTime) + ", "
        s += "openTime: " + str(self.openTime) + ", "
        s += "startTime: " + str(self.startTime) + ", "
        s += "stopTime: " + str(self.stopTime) + ", "
        s += "state: " + str(self.state) + ", "
        s += "floor: " + str(self.floor)
        return s

    def time(self, source, dest):
        t = ((math.fabs(source - dest)) / self.speed) + self.openTime + self.closeTime + self.startTime + self.stopTime

        if self.inMotion:
            t -= self.startTime

        if source == dest:
            t = self.openTime

        return t
