import json
import csv
import Elevator
import Call


def get_flow(self, path):
    rows = []

    try:
        with open(path, 'r') as fl:
            csvr = csv.reader(fl)
            for row in csvr:
                rows.append(row)
    except IOError as e:
        print(e)

    return rows


def write_answers(data, output):
    try:
        with open(output, 'w') as fl:
            csvw = csv.writer(fl)
            csvw.writerows(data)
    except IOError as e:
        print(e)


def initiate_elevator(data):
    elev = Elevator()
    elev.speed = data[1]
    elev.closeTime = data[4]
    elev.openTime = data[5]
    elev.startTime = data[6]
    elev.stopTime = data[7]
    return elev


class Building:

    def __init__(self, building):

        initiation_data = {}
        try:
            with open(building, "r+") as r:
                initiation_data = json.load(r)
        except IOError as e:
            print(e)

        self.min = initiation_data["_minFloor"]
        self.max = initiation_data["_maxFloor"]

        self.elevators = []
        elevators_data = initiation_data["_elevators"]
        for i in range(len(elevators_data)):
            self.elevators.append(initiate_elevator(list(elevators_data[i].values())))

        self.control_panel = []
        for i in range(len(self.elevators)):
            l = []
            self.control_panel.append(l)

    def travel_time(self, elev_num):
        time = 0
        source = self.elevators[elev_num].flour()

        for dest in self.control_panel[elev_num]:
            time += self.elevators[elev_num].time(source, dest)
            source = dest

        return time

    def activate(self, input, output):  # directories
        time = 0
        flow = get_flow(input)

        for step in flow:
            c = Call(step[2], step[3])
            new_time = step[1]
            dt = new_time - time
            self.recalculate(dt)
            decision = self.assign_fastest_option(c)
            time = new_time
            step[5] = decision

        write_answers(output, flow)

    def assign_fastest_option(self, call: Call):
        c_type = call.type
        c_src = call.src
        c_dest = call.dest
        min_time = self.elevators[0].time(c_src, c_dest)
        min_elev = -1
        # find elevators with same state / at zero state
        for (i, elev) in self.elevators:
            if elev.state == 0:
                curr_time = elev.time(c_src, c_dest)
                if min_time > curr_time:
                    min_time = curr_time
                    min_elev = i
            # for same state check dist, if negative, irrelevant
            elif c_type == elev.state:
                dist = (c_src - elev.floor) * elev.state
                # negates when there's no correlation between dist and state
                if dist > 0:
                    curr_time = elev.time(c_src, c_dest)
                    if min_time > curr_time:
                        min_time = curr_time
                        min_elev = i
        # append Call in control panel
        return min_elev

    def recalculate(self, dt):  # dt is the passage of time(d - differnce)
        pass
