#!/usr/bin/env python

# The 'solution' variable should hold the
# solution when the script is done.
#solution = 0
#multiple = 9
# Your code goes here
multiple = 0
max = 100000
i = 1

while i < max:
    if (i % 4 == 0) and (i % 13 == 0) and (i % 14 == 0) and (i % 26 == 0) and (i % 50 == 0): #we need to condition i to be divisible by these numbers: remainder has to be equal to zero
        multiple += 1
        if multiple == 9:
            solution = i
            break
    i += 1

if multiple == 9:
    print(solution)

# Check for the correct answer.
if multiple == 9:
  print("#1 : 9th Multiple ::", "Correct." if solution == 81900 else ("Wrong: " + str(solution)))
