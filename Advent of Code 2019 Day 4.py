#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 19:01:37 2019

@author: joscelynec
"""

#!/bin/python3

"""

You arrive at the Venus fuel depot only to discover

it's protected by a password. The Elves had written

the password on a sticky note, but someone threw

it out.

 

However, they do remember a few key facts about

the password:

 

It is a six-digit number.

The value is within the range given in your puzzle input.

Two adjacent digits are the same (like 22 in 122345).

Going from left to right, the digits never decrease;

they only ever increase or stay the same

(like 111123 or 135679).

Other than the range rule, the following are true:

 

111111 meets these criteria (double 11, never decreases).

223450 does not meet these criteria

(decreasing pair of digits 50).

123789 does not meet these criteria (no double).

How many different passwords within the range given

in your puzzle input meet these criteria?

 

Your puzzle input is 156218-652527

--- Part Two ---

An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

 

Given this additional criterion, but still ignoring the range rule, the following are now true:

 

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.

123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).

111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).

How many different passwords within the range given in your puzzle input meet all of the criteria?

 

Your puzzle input is still 152085-670283.

"""

#Checks if an integer is nondecreasing

def isNonDec(n):

  temp = str(n)

  for i in range(len(temp)-1):

    if int(temp[i])> int(temp[i+1]):

      return False

  return True

#Detects an adjacent pair of digits

def isAdj(n):

  temp = str(n)

  for i in range(len(temp)-1):

    if temp[i] == temp[i+1]:

      return True

  return False

 

  

#Detects an adjacent pair of digits

#not part of a larger sequence

def modifiedAdj(n):

  temp = str(n)

  for i in range(len(temp)-1):

    if temp[i] == temp[i+1]:

      c =temp[i]*2

      d = temp[i]*3

      if c in temp and d not in temp:

        return True

  return False

 

  

#Part 1 count number of passwords and print

ct = 0

for i in range(156218, 652527):

  if isNonDec(i) and isAdj(i):

    ct+=1

print(ct)

 

#Part 2 count number of passwords and print

 

ct = 0

for i in range(156218,652527):

  if isNonDec(i) and modifiedAdj(i):

    ct+=1

print(ct)

 