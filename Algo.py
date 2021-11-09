import json
import Elevator


class bulding:

    def __init__(self, bulding):

        initiation_data = {}
        try:
            with open(bulding, "r+") as r:
                initiation_data = json.load(r)
        except IOError as e:
            print(e)

        self.min = initiation_data["_minFloor"]
        self.max = initiation_data["_maxFloor"]
        self.elevators = initiation_data["_elevators"]

        self.control_panel = []
        for i in range(len(self.elevators)):
            l = []
            self.control_panel.append(l)

        for i in range(len(self.elevators)):
            self.elevators[i] = self.initiate_elvator(self.elevators[i])



    def initiate_elvator(data):
        elev = Elevator()
        elev.speed = data["_speed"]
        elev.closeTime = data["_closeTime"]
        elev.openTime = data["_openTime"]
        elev.startTime = data["_startTime"]
        elev.stopTime = data["_stopTime"]
        return elev



    def TravelTime(self, elev_num):
        time = 0
        surce = self.elevators[elev_num].flour()

        for dest in self.control_panel[elev_num]:
            time += self.elevators[elev_num].Time(surce, dest)
            sursce = dest

        return time

    def Activate(self, input):
        pass#return output
    def Assighn_Fastest_Option(self):
        pass






