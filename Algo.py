import json
import csv
from Elevator import elevator


def initiate_elvator(data):
    elev = elevator()
    elev.speed = data[1]
    elev.closeTime = data[4]
    elev.openTime = data[5]
    elev.startTime = data[6]
    elev.stopTime = data[7]
    return elev


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

        self.elevators = []
        elevators_data = initiation_data["_elevators"]
        for i in range(len(elevators_data)):
            self.elevators.append(initiate_elvator(list(elevators_data[i].values())))

        self.control_panel = []
        for i in range(len(self.elevators)):
            l = []
            self.control_panel.append(l)



    def TravelTime(self, elev_num):
        time = 0
        surce = self.elevators[elev_num].flour()

        for dest in self.control_panel[elev_num]:
            time += self.elevators[elev_num].Time(surce, dest)
            sursce = dest

        return time

    def Activate(self, input):
        time = 0
        try:
            with open(input) as file:
                csvr = csv.reader(file)
        except IOError as e:
            print(e)

        #for row in csvr:
        #    dt
        #    call
        #    recalculate
        #    assign



        pass#return output
    def Assighn_Fastest_Option(self):
        pass






