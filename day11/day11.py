from advent import Session
from hashlib import md5

aoc = Session(2020,11)

with aoc.fp() as fp:
    L = [line.strip() for line in fp.readlines()]
       
def inBounds(x,y,grid):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

def makeAdjDict(grid,ray=False):
    d = {}
    neighbors = [[-1,1],[0,1],[1,1],[-1,0],[1,0],[-1,-1],[0,-1],[1,-1]]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if(grid[y][x] == "."):
                continue
            adj = set()
            for dx,dy in neighbors:
                ax,ay = x+dx, y+dy

                while(ray and inBounds(ax,ay,grid) and (grid[ay][ax] == ".")):
                    ax,ay = ax+dx ,ay+dy

                if(inBounds(ax,ay,grid) and grid[ay][ax] in "#L"):
                    adj.add((ax,ay))
            d[(x,y)] = adj
    return d

def arcaneCount(node,adjDict,nodes,flashing,flashingNodes):
    filled = 0
    for e in adjDict[node]:
        if(e in flashingNodes):
            filled += flashing
        else:
            filled += nodes.get(e,"L") == "#"
    return filled

def arcaneSolve(L,maxFilled=4,ray=False):
    d = makeAdjDict(L,ray=ray)
    g1 = {}
    g2 = {}
    
    flashing = False
    flashingNodes = set(d.keys())

    workingNodes = crystalBuds(flashingNodes,d,maxFilled)
    flashingNodes -= workingNodes
    crystalNodes = set()

    cycle = 0
    while workingNodes:
        newCrystal = set()
        for node in workingNodes:
            filled = arcaneCount(node,d,g1,flashing,flashingNodes)
            if(g1.get(node,"L") == "#" and filled >= maxFilled):
                g2[node] = "L"
            elif(g1.get(node,"L") == "L" and filled == 0):
                g2[node] = "#"
            else:
                g2[node] = g1.get(node,"L")
                newCrystal.add(node)
        
        #Migrate from flashing->working
        for node in newCrystal:
            for e in d[node]:
                if(e not in flashingNodes or e in newCrystal):
                    continue
                g2[e] = "L" if flashing else "#"
                workingNodes.add(e)
                flashingNodes.remove(e)

        workingNodes -= newCrystal
        crystalNodes |= newCrystal

        #print(f"{cycle}: working:{len(workingNodes)} -{len(newCrystal)}-> crystal:{len(crystalNodes)} flashing:{len(flashingNodes)}")

        flashing = not flashing
        g1,g2 = g2,g1
        cycle += 1
    return str(g1).count("#")
    
#Find nodes that will have less than maxFilled flashing partners
def crystalBuds(flashingNodes,adjDict,maxFilled,toCheck=None):
    buds = set()
    toCheck = toCheck if toCheck is not None else flashingNodes
    for node in list(toCheck):
        if(sum(1 for x in adjDict[node] if x in flashingNodes) < maxFilled):
            buds.add(node)
    return buds
        
print("silver:",arcaneSolve(L))
print("gold:",arcaneSolve(L,maxFilled=5,ray=True))
