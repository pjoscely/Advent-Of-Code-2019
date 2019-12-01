#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 13:48:06 2019

@author: joscelynec


--- Day 1: The Tyranny of the Rocket Equation ---
Santa has become stranded at the edge of the Solar System while delivering presents to other planets! To accurately calculate his position in space, safely align his warp drive, and return to Earth in time to save Christmas, he needs you to bring him measurements from fifty stars.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

The Elves quickly load you into a spacecraft and prepare to launch.

At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper. They haven't determined the amount of fuel required yet.

Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

For example:

For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
For a mass of 1969, the fuel required is 654.
For a mass of 100756, the fuel required is 33583.
The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?

Your puzzle answer was 3394106.

--- Part Two ---
During the second Go / No Go poll, the Elf in charge of the Rocket Equation Double-Checker stops the launch sequence. Apparently, you forgot to include additional fuel for the fuel you just added.

Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2. However, that fuel also requires fuel, and that fuel requires fuel, and so on. Any mass that would require negative fuel should instead be treated as if it requires zero fuel; the remaining mass, if any, is instead handled by wishing really hard, which has no mass and is outside the scope of this calculation.

So, for each module mass, calculate its fuel and add it to the total. Then, treat the fuel amount you just calculated as the input mass and repeat the process, continuing until a fuel requirement is zero or negative. For example:

A module of mass 14 requires 2 fuel. This fuel requires no further fuel (2 divided by 3 and rounded down is 0, which would call for a negative fuel), so the total fuel required is still just 2.
At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2). 216 then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel. So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.
What is the sum of the fuel requirements for all of the modules on your spacecraft when also taking into account the mass of the added fuel? (Calculate the fuel requirements for each module separately, then add them all up at the end.)

Your puzzle answer was 5088280.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

#Spacecraft modules
l = [94735, 80130, 127915, 145427, 89149, 91232, 100629, 97340, 86278, 87034, 147351, 123045, 91885, 85973, 64130, 113244, 58968, 76296, 127931, 98145, 120731, 98289, 110340, 118285, 60112, 57177, 58791, 59012, 66950, 139387, 145378, 86204, 147082, 84956, 134161, 148664, 74278, 96746, 144525, 81214, 70966, 107050, 134179, 138587, 80236, 139871, 104439, 64643, 145453, 94791, 51690, 94189, 148476, 79956, 81760, 149796, 109544, 57533, 142999, 126419, 115434, 57092, 64244, 109663, 94701, 109265, 145851, 95183, 84433, 53818, 106234, 127380, 149774, 59601, 138851, 54488, 100877, 136952, 61538, 67705, 60299, 130769, 113176, 106723, 133280, 111065, 63688, 139307, 122703, 60162, 89567, 63994, 66608, 126376, 136052, 112255, 98525, 134023, 141479, 98200]


#Computes fuel needed for fuel
def comp_fuel(f):
  ans = 0
  f = f//3-2
  while f > 0:
    ans+=f
    f = f//3-2
  return ans
print(comp_fuel(654))#test a value


#Compute total fuel = modules + fuel needed for each module's fuel
ans1 = 0
ans2 = 0
for n in l:#iterate over the modules list
  temp = n//3 -2
  ans1+=temp
  ans2+= temp + comp_fuel(temp)
print(ans1,ans2)#Display answers to Parts 1,2





