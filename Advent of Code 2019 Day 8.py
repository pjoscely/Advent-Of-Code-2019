#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 17:52:46 2019

@author: joscelynec
"""

A = open('/Users/joscelynec/Desktop/Advent Of Code/Day8.txt').read().split('\n')
#return number of 0s, 1s, 2s
def getLayerData(layer):
    z = 0
    o = 0
    t = 0
    for d in layer:
        if d == str(0):
            z+=1
        elif d ==str(1):
            o+=1
        else:
            t+=1
    return (z,o,t)
#create flat string of data
s = str(A[0])

#extract layers into list

indx = 0
ls = []
for _ in range(100):
    ls.append(s[indx:indx+150])
    indx+=150

"""
"Uncomment this for Part 1
for l in ls:
    print(getLayerData(l))

Inspecting print out
(7, 21, 122) has fewest 0s
21*122 = 2562<---- Part 1 answer
That's the right answer! You are one gold star closer to rescuing Santa.
"""  
"""
--- Part Two ---
Now you're ready to decode the image. The image is rendered by stacking the layers and aligning the pixels with the same positions in each layer. The digits indicate the color of the corresponding pixel: 0 is black, 1 is white, and 2 is transparent.

The layers are rendered with the first layer in front and the last layer in back. So, if a given position has a transparent pixel in the first and second layers, a black pixel in the third layer, and a white pixel in the fourth layer, the final image would have a black pixel at that position.

For example, given an image 2 pixels wide and 2 pixels tall, the image data 0222112222120000 corresponds to the following image layers:

Layer 1: 02
         22

Layer 2: 11
         22

Layer 3: 22
         12

Layer 4: 00
         00
Then, the full image can be found by determining the top visible pixel in each position:

The top-left pixel is black because the top layer is 0.
The top-right pixel is white because the top layer is 2 (transparent), but the second layer is 1.
The bottom-left pixel is white because the top two layers are 2, but the third layer is 1.
The bottom-right pixel is black because the only visible pixel in that position is 0 (from layer 4).
So, the final image looks like this:

01
10
What message is produced after decoding your image?
"""
#create empty image string
image = ""
test = '0222112222120000'
testLs = ['0222','1122','2212','0000']
#Simple helper function
def getColor(l):
    for digit in l:
        if digit == '0':
            return '0'
        elif digit == '1':
            return '1'
        elif digit == '2':
            continue
for indx in range(4):
    temp = []
    for l in testLs:
        temp.append(str(l[indx]))
    image += getColor(temp)
  
print(image)

"""
Test run ok
Run Part 2
 """ 
image = "" 
for indx in range(150):
    temp = []
    for l in ls:
        temp.append(str(l[indx]))
    image += getColor(temp) 
#Render the message
for indx in range(0,150,25):
    print(image[indx:indx+25])
"""
1111011110100001110010001
0001010000100001001010001
0010011100100001110001010
0100010000100001001000100
1000010000100001001000100
1111010000111101110000100
When rendered in a black and white 
grid spells 
ZFLBY
See Day 8 Answer PDF
That's the right answer! You are one gold star closer to rescuing Santa.
"""







         
    