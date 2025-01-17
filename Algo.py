import json
import csv
import math

import Elevator
import Call


def get_flow(path):
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
    elev = Elevator.Elevator()
    elev.speed = data[1]
    elev.closeTime = data[4]
    elev.openTime = data[5]
    elev.startTime = data[6]
    elev.stopTime = data[7]
    return elev


def add_ascend(lst, val):
    i = 0
    while i < len(lst) and lst[i] < val:
        i += 1
    lst.insert(i, val)


def add_descend(lst, val):
    i = 0
    while i < len(lst) and lst[i] > val:
        i += 1
    lst.insert(i, val)


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
            self.control_panel.append([])

    def travel_time(self, elev_num, call: Call):
        time = 0
        source = self.elevators[elev_num].floor
        missions = self.control_panel[elev_num]

        if self.elevators[elev_num].state == 1:
            i = 0
            while (i < len(missions)) & (missions[i] < call.src):
                dest = missions[i]
                time += self.elevators[elev_num].time(source, dest)
                source = dest
                i += 1
        else:
            i = 0
            while (i < len(missions)) and (missions[i] > call.src):
                dest = missions[i]
                time += self.elevators[elev_num].time(source, dest)
                source = dest
                i += 1

        time += self.elevators[elev_num].time(source, call.src)

        return time

    def activate(self, input, output):  # directories
        time = 0
        flow = get_flow(input)

        for step in flow:
            if len(step) == 0:
                continue

            c = Call.Call(int(step[2]), int(step[3]))
            new_time = float(step[1])
            dt = new_time - time
            self.recalculate(dt)
            if c.is_legit(self.min, self.max):
                decision = self.assign_fastest_option(c)
                step[5] = decision
            time = new_time

        write_answers(flow, output)

    def assign_fastest_option(self, call: Call):
        c_type = call.type
        c_src = call.src
        c_dest = call.dest
        min_time = math.inf
        min_elev = 0
        # find elevators with same state / at zero state
        for i in range(len(self.elevators)):
            elev = self.elevators[i]

            if elev.state == 0:
                curr_time = self.travel_time(i, call)
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
        elev = self.elevators[min_elev]
        elev_missions = self.control_panel[min_elev]
        if elev.state == 1:
            add_ascend(elev_missions, c_src)
            add_ascend(elev_missions, c_dest)
        elif elev.state == -1:
            add_descend(elev_missions, c_src)
            add_descend(elev_missions, c_dest)
        else:
            elev.state = c_type
            elev_missions.append(c_src)
            elev_missions.append(c_dest)

        return min_elev

    def recalculate(self, dt):  # dt is the passage of time(d - difference)
        for i in range(len(self.control_panel)):
            try:
                self.advance(i, dt)
            except:
                pass
            finally:
                if len(self.control_panel[i]) == 0:
                    self.elevators[i].state = 0

    def advance(self, i, dt):
        elev = self.elevators[i]

        while dt > 0:  # while there is time
            dest = self.control_panel[i][0]

            t = elev.time(elev.floor, dest)
            # if possible go to the next location
            if t <= dt:
                elev.floor = dest
                self.control_panel[i].pop(0)
                dt -= t
            # if you can reach destination but not yet can stop and open
            elif t - elev.openTime - elev.stopTime <= dt:
                elev.floor = dest
                break
            # if you cant reach at all
            else:
                dt -= elev.startTime + elev.closeTime  # close and start moving
                if dt > 0:  # if you at least managed that
                    elev.inMotion = True  # you will advance a bit
                    if dest - elev.floor > 0:
                        elev.floor += dt * elev.speed  # going upwards
                    else:
                        elev.floor -= dt * elev.speed  # downwards
