from advent import Session

aoc = Session(2020,15)

with aoc.fp() as fp:
    L = [int(x) for x in fp.read().strip().split(",")]
def solve(rounds,L):
    spoken = {}
    cycle = 1
    new = False
    for e in L:
        new = e not in spoken
        if(e in spoken):
            spoken[e][0] = spoken[e][1]
            spoken[e][1] = cycle
        else:
            spoken[e] = [0,cycle]
        n = e
        cycle += 1

    while cycle < rounds+1:
        if(new):
            n = 0
        else:
            n = spoken[n][1] - spoken[n][0]
            
        new = n not in spoken
        if(n in spoken):
            spoken[n][0] = spoken[n][1]
            spoken[n][1] = cycle
        else:
            spoken[n] = [0,cycle]
        cycle += 1
    return n
silver = solve(2020,L)
print("silver:",silver)
gold = solve(30000000,L)
print("gold:",gold)
 
