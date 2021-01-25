from advent import Session
from hashlib import md5
import math

aoc = Session(2020,12)

with aoc.fp() as fp:
    L = [line.strip() for line in fp.readlines()]

silver,gold = 0,0

directions = [(1,0),(0,-1),(-1,0),(0,1)]
dIndex = 0
x,y = 0,0
for line in L:
    d = line[0]
    n = int(line[1:])
    if(d == "N"):
        y += n
    elif(d == "S"):
        y -= n
    elif(d == "E"):
        x += n 
    elif(d== "W"):
        x -= n
    elif(d == "L"):
        spots = n//90
        dIndex = (dIndex-spots)%4
    elif(d == "R"):
        spots = n//90
        dIndex = (dIndex+spots)%4
    elif(d == "F"):
        dx,dy = directions[dIndex]
        x += dx*n
        y += dy*n
silver = abs(x)+abs(y)

x,y = 0,0
wx,wy = 10,1
for line in L:
    d = line[0]
    n = int(line[1:])
    if(d == "N"):
        wy += n
    elif(d == "S"):
        wy -= n
    elif(d == "E"):
        wx += n 
    elif(d== "W"):
        wx -= n
    elif(d == "L"):
        spots = n//90
        if(spots == 1):
            wx,wy = -wy,wx
        elif(spots == 2):
            wx,wy = -wx,-wy
        elif(spots == 3):
            wx,wy = wy,-wx
    elif(d == "R"):
        spots = n//90
        if(spots == 1):
            wx,wy = wy,-wx
        elif(spots == 2):
            wx,wy = -wx,-wy
        elif(spots == 3):
            wx,wy = -wy,wx
    elif(d == "F"):
        x += (wx * n)
        y += (wy * n)

gold = abs(x)+abs(y)
       

print("silver:",silver)
print("gold:",gold)
