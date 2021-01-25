from advent import Session
import itertools

aoc = Session(2020,9)

with aoc.fp() as fp:
    L = [int(line.strip()) for line in fp.readlines()]

silver = 0
gold = 0
instr = []

nSet = set(L[:25])
i = 25
while i < len(L):
    valid = any((L[i] - e) in nSet for e in nSet)
    if(not valid):
        break
    nSet.remove(L[i-25])
    nSet.add(L[i])
    i += 1
firstInvalid = L[i]

def slinky(L,target):
    i,k = 0,0
    z = L[i]
    while z != target:
        if(z < target):
            k += 1
            z += L[k]
        else:
            z -= L[i]
            i += 1
    return min(L[i:k+1]) + max(L[i:k+1])
                    
gold = slinky(L,firstInvalid)
print("silver:",firstInvalid)
print("gold:",gold)
