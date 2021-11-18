import Algo

def simulate(jsn, input, output):
    bld = Algo.Building(jsn)
    bld.activate(input, output)



if __name__ == '__main__':
    jsn = r"C:\Users\S\OneDrive\Desktop\Ex1_input\Ex1_Buildings\B5.json"
    inp = r"C:\Users\S\OneDrive\Desktop\Ex1_input\Ex1_Calls\Calls_c.csv"
    out = r"C:\Users\S\OneDrive\Desktop\Ex1_input\output\output03.csv"
    simulate(jsn, inp, out)

