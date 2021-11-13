# Ex1_OOP
Second assignment on ObjectOrientedPrograming with python

### Plan
For now, we will write a simpler algorithm that will keep a time parameter
and would traverse the input file row by row and in each iteration it would:
+ advance the time parameter by the time passed until the next Call
+ recalculate the states of all elevators
+ Assign the new Call in a clever way

I know it's an online algorithm but to take advantage of all the data at once is
actually harder, we can update it to an offline version as asked later on

I suggest that each elevator would be in either of 3 states:
+ rest coded by 0
+ going up coded by 1      only picking up travelers that goes in its direction
+ going down coded by -1    same

An elevator at rest would change its state according to its first new Call

We would have an arrayList like in the last assignment

state 1 elevators would get new calls in ascended order and a
 state -1 elevators would get new calls in descended order
