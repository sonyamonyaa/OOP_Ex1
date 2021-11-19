# Ex1_OOP
Second assignment on ObjectOrientedPrograming with python

## Plan
simple algorithm that keeps a time parameter
and would traverse the input file row by row and in each iteration it would:
+ advance the time parameter by the time passed until the next Call
+ recalculate the states of all elevators
+ Assign the new Call in a clever way

similar to an online algorithm but to take advantage of all the data at once is
actually harder, so we built some kind of simulation using 3 classes - Call, Elevator and Algo.

### Elevator
represents an elevator, holding the time parameters 
(speed, closing time, starting time etc.) 
and calculates the overall time of an elevator.

Each elevator would be in either of 3 states:
+ rest coded by 0
+ going up coded by 1      only picking up travelers that goes in its direction
+ going down coded by -1    same

An elevator at rest would change its state according to its first new Call

We would use a list

State "1" elevators would get new calls in ascended order and a
state "-1" elevators would get new calls in descended order

can be tested by making comparisons of given parameters and check the time
### Call
Represents an elevator call, holds the parameters source, destination and its type (up/down). 
also checks legitimacy of a call within given range (max and min floors of a building)

Can be tested by making comparisons of given parameters
and checking legitimacy within range and out of range

### Algo
The algorithm class which holds several functions and 
the building class to provide the optimal solutions.

##### functions
+ get_flow - reads the csv input.
+ write_answers - writes the csv output, with 
the allocation for each call
+ initiate elevator - builds an elevator object 
according to given data (json file)
+ add ascend/descend - each adds a call to a list 
in ascending / descending order

##### Building
+ init - creates a list of elevators from given data and a control panel of pending calls for each elevator
+ travel time - calculates the overall travel time of an elevator with given call
+ activate - reads the given calls file and for each call assigns an elevator and in the end writes the output 
+ assign fastest option - the assigning function, uses the travel time to find the optimal elevator of a given call and appends accordingly the call to control panel
+ recalculate - calculates the passage of time
+ advance - updates the elevator locations

##### the data folder contains:
+ call cases  
+ instances of building in jason format
+ actuall results of the program
+ an ampty csv file for output 
