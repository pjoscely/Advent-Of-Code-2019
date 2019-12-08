#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 02:52:28 2019

@author: joscelynec
--- Day 6: Universal Orbit Map ---
You've landed at the Universal Orbit Map facility on Mercury. 
Because navigation in space often involves transferring between orbits, 
the orbit maps here are useful for finding efficient routes between, f
or example, you and Santa. You download a map of the local orbits 
(your puzzle input).

Except for the universal Center of Mass (COM), every object in space 
is in orbit around exactly one other object. An orbit looks roughly like this:

                  \
                   \
                    |
                    |
AAA--> o            o <--BBB
                    |
                    |
                   /
                  /
In this diagram, the object BBB is in orbit around AAA. The path that BBB 
takes around AAA (drawn with lines) is only partly shown. In the map data, 
this orbital relationship is written AAA)BBB, which means "BBB is in orbit 
    around AAA".

Before you use your map data to plot a course, you need to make sure it wasn't 
corrupted during the download. To verify maps, the Universal Orbit Map facility
 uses orbit count checksums - the total number of direct orbits 
 (like the one shown above) and indirect orbits.

Whenever A orbits B and B orbits C, then A indirectly orbits C. 
This chain can be any number of objects long: if A orbits B, B orbits C, 
and C orbits D, then A indirectly orbits D.

For example, suppose you have the following map:

COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
Visually, the above map of orbits looks like this:

        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I
In this visual representation, when two objects are connected by a line, 
the one on the right directly orbits the one on the left.

Here, we can count the total number of orbits as follows:

D directly orbits C and indirectly orbits B and COM, a total of 3 orbits.
L directly orbits K and indirectly orbits J, E, D, C, B, and COM, 
a total of 7 orbits.
COM orbits nothing.
The total number of direct and indirect orbits in this example is 42.

What is the total number of direct and indirect orbits in your map data?
"""
#Test data solution
test = ['*)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']
#create set of all objects "*'
t = set()
for i in range(len(test)):
    t.add(test[i][0:1])
    t.add(test[i][2:])  
print(t)
#finds a leaf's immediate parent
def findLeafParentVer1(letter, data):
    for item in data:
        if letter == item[2:]:
            return item[0:1]
    return '*'
#given a letter build a string back to root 
def findPathToRootVer1(letter, data):
    path =str(letter)
    if letter == '*':
        return '*'
    else:
        temp = findLeafParentVer1(letter, data)
        while(temp != '*'):
            path= temp+path
            temp = findLeafParentVer1(temp, data)
    return '*'+path

ls = set()
for it in t:
    ls.add(findPathToRootVer1(str(it), test))

ct = 0
print(ls)
for _ in ls:
    ct+=len(_)-1
print(ct)


"""
Beta test 1 looks good for Part 1 
"""
#Input puzzle data 
A = open('/Users/joscelynec/Desktop/Advent Of Code/Day6.txt').read().split('\n')
p = set()
#print(A)

#Create set of all objects of the form '***'
for i in range(len(A)):
    p.add(A[i][0:3])
    p.add(A[i][4:])

#finds a leaf's immediate parent
def findLeafParentVer2(object, data):
    #in case object = 'COM'
    if object == 'COM':
        return object
    for item in data:
        if object == str(item[4:]):
            return str(item[0:3]) 

#given a object build a string back to root 
def findPathToRootVer2(object, data):
    path =str(object)
    if object == 'COM':
        return 'COM'
    else:
        temp = findLeafParentVer2(object, data)
        while(temp != 'COM'):
            path= temp+path
            temp = findLeafParentVer2(temp, data)
    return 'COM'+path

#Get all paths
paths = set()
for code in p:
    paths.add(findPathToRootVer2(str(code), A))
#count all direct and indirect orbits

ct = 0
for pth in paths:
    temp = int(len(pth)/3)-1
    ct+=temp
print(ct)
"""
Your puzzle answer was 135690.

The first half of this puzzle is complete! It provides one gold star: *
**** Interesting to note Part 1 takes ~20 secs ****
--- Part Two ---
Now, you just need to figure out how many orbital transfers you (YOU) 
need to take to get to Santa (SAN).

You start at the object YOU are orbiting; your destination is the object 
SAN is orbiting. An orbital transfer lets you move from any object to 
an object orbiting or orbited by that object.

For example, suppose you have the following map:

COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN
Visually, the above map of orbits looks like this:

                          YOU
                         /
        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I - SAN
In this example, YOU are in orbit around K, and SAN is in orbit around I. 
To move from K to I, a minimum of 4 orbital transfers are required:

K to J
J to E
E to D
D to I
Afterward, the map of orbits looks like this:

        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I - SAN
                 \
                  YOU
What is the minimum number of orbital transfers required to 
move from the object YOU are orbiting to the object SAN is orbiting? 
(Between the objects they are orbiting - not between YOU and SAN.)
"""
#Find paths for 'YOU' and 'SAN'
for item in paths:
    if 'YOU' == item[len(item)-3:]:
        print(item)
    if 'SAN' == item[len(item)-3:]:
        print(item)
#Paths found COM to YOU and SAN used in Part 2 to avoid recomputing Part 1       
YOU_PATH = 'COMX6MHRLKMXSFMR82WC6TV1WD7X3F714TCLPR165DWGKV1CNSP8KMN36WGTDRWQHTP8LJ3GL61Q6D2T4FJBFSG2WQWRQ8TZ931SWC7RT6P3YN8NYPR2J9SQJQFD38WCDTJ13FB7DSJL758WHJPJW5D84P43Q8DL11SCVY1RWYL3YTJ6SVMSTGSWRTP7BSSDJZW2M231WLLGNTTYKQNVKP3XXC7ZTV53BXNGWPJXJB5XSGMRLW3Q1R7J97THZMWJBLBX3181NYNP7YBQZRDLWRFS1JF1D6MDQPT87C7X3L4NFQ56WN9N2GXCWMR88BXG2VN2V75LKV2KDJ6PYHPCMV9BRGJQKP1D73814QKZNV17RJGWGDV3K5L463TYGQ1X967N6GLFGDS5YQ9YSGBYNML1LWQ8MXFTZQ9WYST98PVC51KB777S5FDG6WF3HXN26QKVDJSNM8YMD6VK9T48TK26CVTTH2S23HJCGB8W7KCNFPSXFH8XY7D959VVZ1BY24PLNQGWCWBPXW49WY15L1CW1VXFLQZFS8LB1FM4XW68X7PQV6BFQ3FZPGPV4D16BVY5XNMCZCFVLX6B2MP3M1KPFKG8GLW11JDRL4L359VXGFDC7D4MS17K7HZZCCN42DWZLKVXHP7WXKWDF5GWJXVSTM5M62BCZLXLTKH8DSKZG8KV4G6R2V9WRVP469XS26P6QV2227DF3P217YM5VZL4J146H3Q965QXB1P2Q93GMS837Q8K8NH2NJ4CK9Z5YOU'    
COM_PATH = 'COMX6MHRLKMXSFMR82WC6TV1WD7X3F714TCLPR165DWGKV1CNSP8KMN36WGTDRWQHTP8LJ3GL61Q6D2T4FJBFSG2WQWRQ8TZ931SWC7RT6P3YN8NYPR2J9SQJQFD38WCDTJ13FB7DSJL758WHJPJW5D84P43Q8DL11SCVY1RWYL3YTJ6SVMSTGSWRTP7BSSDJZWGLBTJN25TDSVQVLSDZPCJFG3WNYJ1JKT7WQ7R71ZKF9VCJ2PYRLCHBM6854BCC3MWJC9JRN463DZP933R3T5K3C7CSQK5DD6DMHM8NM1WCJXY2ZZVV2LNXGGKK61YR173VF91TLVJFQK7MPDJTF3S2T6CGDNR6XHWBVZHJ2NG1WSSWQ33ZDL3FX41DMDDGQCG2NH68CWVDFVSVPHQZQZ26ZPLZWPFXS6LL236ZCCXSQJDF21QPMGKXQR7P3PJ64XQRJKBDCNWF71H4KC17KLGB862Q4Z9FZV9WMH74S9L39BW4B5J5WLW5M542CLVHDD2SAN'

#Find branch point indx
indx = 0
while(YOU_PATH[indx:indx+3]==COM_PATH[indx:indx+3]):
    #print(YOU_PATH[indx:indx+3],int(indx/3))
    indx+=3
indx = int(indx/3)-1
#Find paths from branch point to YOU and SAN respectively
yTail = YOU_PATH[3*indx:]
cTail = COM_PATH[3*indx:]

#Reduce each tail by 2 to compute mininum number or transfers 
print(int(len(yTail)/3-2 + len(cTail)/3-2))
"""
Your puzzle answer was 298.
Both parts of this puzzle are complete! They provide two gold stars: **
"""
