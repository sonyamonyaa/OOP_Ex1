from Elevator import Elevator

el0 = Elevator()
el1 = Elevator(1, 1, 1, 1, 1)







if __name__ == '__main__':
    print(el1.speed)
    print(el0.speed)
    print(el1.time(2, 5)) #should be 3 +1+1+1+1 = 7
    print(el1, '\n', el0)
    print(el1.time(0, 2)) #should be 2 +1+1+1 = 5
    print(el1.time(0,0)) # should be 2