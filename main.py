import Algo

def simulate(jsn, input, output):
    bld = Algo.Building(jsn)
    bld.activate(input, output)



if __name__ == '__main__':
    jsn = r"C:\Users\ישראל\Downloads\computer sincse\OOP\Assignments\Ex1\data\Ex1_input\Ex1_Buildings\B1.json"
    inp = r"C:\Users\ישראל\Downloads\computer sincse\OOP\Assignments\Ex1\OOP_2021-main\Assignments\Ex1\data\Ex1_Calls_case_2_a.csv"
    out = r"C:\Users\ישראל\Downloads\computer sincse\OOP\Assignments\Ex1\exp"
    simulate(jsn, inp, out)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
