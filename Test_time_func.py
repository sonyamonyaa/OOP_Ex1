import Algo
import Call

Path = r"C:\Users\ישראל\Downloads\computer sincse\OOP\Assignments\Ex1\data\Ex1_input\Ex1_Buildings\B4.json"

bld = Algo.Building(Path)


if __name__ == '__main__':

    #making sure everything is fine with the initiation
    print(bld.min, " ", bld.max)
    for i in bld.elevators:
        print(i, '\n')
    print(bld.control_panel)


    #building the acctual test for the 'travel_time' function
    elevs = bld.elevators

    for i in range(len(elevs)):
        elevs[i].floor = i

    # simulating case
    calls = [[1,3,5,6],
             [-1,-3,-7],
             [10, 20],
             [100],
             []]

    elevs[0].state = 1
    elevs[1].state = -1
    elevs[2].state = 1
    elevs[3].state = 1
    elevs[4].state = 0

    #distrebuting elevators
    for i in range(len(calls)):
        bld.control_panel[i] = calls[i]

    new_calls = [4, 0, 15, 50, 4]

    expected_result = [bld.elevators[0].time(0,1) + bld.elevators[0].time(1,3) + bld.elevators[0].time(3,4),
                       bld.elevators[1].time(1, 0),
                       bld.elevators[2].time(2,10) + bld.elevators[2].time(10, 15),
                       bld.elevators[3].time(3, 50),
                       bld.elevators[4].time(4,4)]

    print(expected_result[0] == bld.travel_time(0, Call.Call(new_calls[0], 5)))
    print(expected_result[1] == bld.travel_time(1, Call.Call(new_calls[1], -2)))
    print(expected_result[2] == bld.travel_time(2, Call.Call(new_calls[2], 16)))
    print(expected_result[3] == bld.travel_time(3, Call.Call(new_calls[3], 51)))
    print(expected_result[4] == bld.travel_time(4, Call.Call(new_calls[4], 5)))

    #tesr for 'recalculate
    for elev in bld.elevators:
        print(elev)
    print(bld.control_panel)



    bld.recalculate(10)

    expected_remaning_calls = [[1,3,5,6],
                               [-1, -3,-7],
                               [20],
                               [100],
                               []]


    for i in range(len(bld.elevators)):
        print(expected_remaning_calls[i] == bld.control_panel[i])

    for i in range(len(bld.elevators)):
        print(bld.elevators[i].floor)

