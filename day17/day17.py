from advent import Session
import collections
import itertools
import time

aoc = Session(2020,17)

with aoc.fp() as fp:
    L = [line.strip() for line in fp.readlines()]
silver,gold = 0,0

def init_space(L,dim):
    space = {}
    #fill space with (x,y,some 0's) to match dim
    r = (0,)*(dim-2)
    for y,line in enumerate(L):
        for x,c in enumerate(list(line)):
            if(c == "#"):
                space[(x,y,*r)] = "#"
    return space
        
        
def neighbors(point,space,dim):
    r = [-1,0,1]
    for p in itertools.product(r,repeat=dim):
        if not all(e == 0 for e in p):
            yield tuple(sum(e) for e in zip(point,p))
    
def step(space,dim,consider):
    ma,mi = 0,0
    for point in space.keys():
        for p in neighbors(point,space,dim):
            ma = max(ma,max(p))
            mi = min(mi,min(p))
            consider[p] += 1
    next_space = {}
    for point,count in consider.items():
        consider[point] = 0
        c = space.get(point,".")
        if c == "#" and 2 <= count <= 3:
            next_space[point] = "#" 
        elif c == "." and count == 3:
            next_space[point] = "#"
    return next_space
            
def six_cycle(L,dim):
    space = init_space(L,dim)
    consider = collections.defaultdict(int)
    for _ in range(6):
        space = step(space,dim,consider)        
    return sum(1 for x in space.values() if x == "#")

"""
#n-dimensional progression
for d in range(3,10):
    t = time.time()
    print(f"Dim {d}: {six_cycle(L,d)} time: {time.time()-t}")
"""
    
silver = six_cycle(L,3)
print("silver:",silver)
gold = six_cycle(L,4)
print("gold:",gold)
