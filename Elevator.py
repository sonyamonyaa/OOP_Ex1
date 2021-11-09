class elevator:
    def __init__(self) -> None:
        self.speed = 0
        self.closeTime = 0
        self.openTime = 0
        self.startTime = 0
        self.stopTime = 0

        self.state = 0 #0 -resting, -1 -gowing down, 1 -going up
        self.flour = 0