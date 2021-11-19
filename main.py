import Algo

def simulate(jsn, input, output):
    bld = Algo.Building(jsn)
    bld.activate(input, output)



if __name__ == '__main__':
    jsn = input("enter the diractorie to the jason file:")
    inp = input("enter the diractory to the Calls file:")
    out = input("enter the diractory to the output file(csv):")
    simulate(jsn, inp, out)
