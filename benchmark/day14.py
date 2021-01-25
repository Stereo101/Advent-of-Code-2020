from advent import Session
from hashlib import md5
import math
import itertools

aoc = Session(2020,14)

with aoc.fp() as fp:
    L = [line.strip() for line in fp.readlines()]

silver,gold = 0,0

def mask(n,m):
    r = list(bin(n)[2:])
    r = ["0"]*(36-len(r)) + r
    for i,c in enumerate(list(m)):
        if(c != "X"):
            r[i] = c 
    return int("".join(r),2)

def amask(n,m):
    r = list(bin(n)[2:])
    r = ["0"]*(36-len(r)) + r
    for i,c in enumerate(list(m)):
        if(c == "X"):
            r[i] = c 
        elif(c == "0"):
            pass
        elif(c == "1"):
            r[i] = "1"
    return "".join(r)
        
def mGen(m):
    xCount = m.count("X")
    for perm in range(2**xCount):
        z = list(m)
        for i in range(len(z)):
            if(z[i] == "X"):
                z[i] = "1" if (perm & 1) else "0"
                perm = perm >> 1
        yield int("".join(z),2)
        
def applyMem(a,n,mem):
    for adr in mGen(a):
        mem[adr] = n

mem = {}
for line in L:
    if(line.startswith("mask")):
        m = line.split("mask = ")[1]
    elif(line.startswith("mem")):
        adr = int(line.split("mem[")[1].split("]")[0])
        n = int(line.split(" = ")[1])
        mem[adr] = mask(n,m)
silver = sum(mem.values())

mem = {}
for line in L:
    if(line.startswith("mask")):
        m = line.split("mask = ")[1]
    elif(line.startswith("mem")):
        adr = int(line.split("mem[")[1].split("]")[0])
        n = int(line.split(" = ")[1])
        adr = amask(adr,m)
        applyMem(adr,n,mem)
gold = sum(mem.values())
 
print("silver:",silver)
#aoc.solution(1,silver)
print("gold:",gold)
#aoc.solution(2,gold)
