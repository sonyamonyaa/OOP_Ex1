import Algo

def simulate(jsn, input, output):
    bld = Algo.Building(jsn)
    bld.activate(input, output)



if __name__ == '__main__':
    jsn = r"C:\Users\ישראל\Downloads\computer sincse\OOP\Assignments\Ex1\data\Ex1_input\Ex1_Buildings\B5.json"
    inp = r"C:\Users\ישראל\Downloads\computer sincse\OOP\Assignments\Ex1\data\exp\CallsB.csv"
    out = r"C:\Users\ישראל\Downloads\computer sincse\OOP\Assignments\Ex1\data\exp\out.csv"
    simulate(jsn, inp, out)
