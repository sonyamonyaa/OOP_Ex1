import json
from Algo import Building

Path = r"C:\Users\ישראל\Downloads\computer sincse\OOP\Assignments\Ex1\data\Ex1_input\Ex1_Buildings\B1.json"

initiation_data = {}
try:
    with open(Path, "r+") as r:
        initiation_data = json.load(r)
except IOError as e:
    print(e)

# min = initiation_data["_minFloor"]
# max = initiation_data["_maxFloor"]
# elevators = initiation_data["_elevators"]

bld = Building(Path)

if __name__ == '__main__':
    # print(initiation_data)
    # print(type(initiation_data))
    # print(max, min)
    # print(elevators)
    # print(elevators[0].values())
    # print(bld.min, bld.max)
    # print(bld.elevators[0])
    print(bld.control_panel)

    # print(bld.max, bld.min)
