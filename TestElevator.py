from Elevator import Elevator

el0 = Elevator()
el1 = Elevator(1, 1, 1, 1, 1)







if __name__ == '__main__':
    print(el1.speed)
    print(el0.speed)
    print(el1.time(2, 5))
    print(el1, el0)