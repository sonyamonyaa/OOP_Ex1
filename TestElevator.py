from Elevator import elevator

el0 = elevator()
el1 = elevator(1,1,1,1,1)







if __name__ == '__main__':
    print(el1.speed)
    print(el0.speed)
    print(el1.Time(2,5))
    print(el1, el0)