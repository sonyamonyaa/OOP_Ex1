# Ex1_OOP
Second essighnment on ObjectOrientedPrograming with python

### Plan
for now we will write a simpler algorithm that will keep a time parameter
and would traverse the input file row by row and in each iteration it would:
+ advance the time parameter by the time passed until the next call
+ recalculate the states of all elvators
+ Assighn the new call in a clever way

I know its an online algorithm but to take advantage of all of the data at once is
actually harder, we can update it to an offline version as asked later on

I suggest that each alvator would be in either of 3 states:
+ rest coded by 0
+ gowing up coded by 1      only picking up travelers that goes in its diraction
+ going down coded by -1    same

An elvator at rest woud change its state acording to its first new call

We would have an arrayList like in the last essighnment

state 1 elevators would get new calls in ascended order and a
 state -1 elevators would get new calls in dscended order
