import json
import Elevator


# PLAN!!!
#jason - intiate
#distrabusion maybe by planning
#                  for i in calls:
#                      advance time by call
#                      re calculate elvator states
#                      Assighn()
#


def initiate_elvator(data):
    elev = Elevator()
    #.....


def Assighnment(bulding, calls, output):

    initiation_data = {}
    try:
        with open(bulding, "r+") as r:
            initiation_data = json.load(r)
    except IOError as e:
        print(e)

    min = initiation_data["_minFloor"]
    max = initiation_data["_maxFloor"]
    elevators = initiation_data["_elevators"]

    control_panel = []
    for i in range(len(elevators)):
        l = []
        control_panel.append(l)

    for i in range(len(elevators)):
        elevators[i] = initiate_elvator(elevators[i])


