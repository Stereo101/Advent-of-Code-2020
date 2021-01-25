from advent import Session
from functools import reduce
aoc = Session(2020,24)

with aoc.fp() as fp:
    L = [x.strip() for x in fp.readlines()]

dir_map = {"e":(1,0),"se":(0,-1),"ne":(1,1),"sw":(-1,-1),"w":(-1,0),"nw":(0,1)}
A = []
build = ""
for line in L:
    a = []
    for c in line:
        build += c
        if build in dir_map:
            a.append(build)
            build = ""
    A.append(a)

def adj(e,nw):
    yield (e+1,nw)
    yield (e+1,nw+1)
    yield (e,nw+1)
    yield (e-1,nw)
    yield (e,nw-1)
    yield (e-1,nw-1)

def round(d):
    to_inspect = set()
    for e,nw in d:
        for p in adj(e,nw):
            to_inspect.add(p)
    new_d = set()
    for e,nw in to_inspect:
        count = sum(1 for pair in adj(e,nw) if pair in d)
        if((e,nw) in d):
            if not (count == 0 or count > 2):
                new_d.add((e,nw))
        elif count == 2:
            new_d.add((e,nw))
    return new_d
        
d = set()
for line in A:
    p = reduce(lambda p1,p2:(p1[0]+p2[0],p1[1]+p2[1]),(dir_map[z] for z in line))
    if(p in d):
        d.remove(p)
    else:
        d.add(p)

silver = len(d)
    
for r in range(100):
    d = round(d)
    
gold = len(d)


print("silver:",silver)
print("gold:",gold)
