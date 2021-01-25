from advent import Session

aoc = Session(2020,22)

with aoc.fp() as fp:
    L = [line.strip() for line in fp.readlines()]

d1 = [int(n) for n in L[1:L.index("")]]
d2 = [int(n) for n in L[L.index("Player 2:")+1:]]

def combat(d1,d2):
    d1,d2 = d1.copy(),d2.copy()
    while len(d1) > 0 and len(d2) > 0:
        c1,c2 = d1.pop(0),d2.pop(0)
        if(c1 > c2):
            d1 += [c1,c2]
        else:
            d2 += [c2,c1]
    return max(d1,d2)

def rec_combat(d1,d2):
    d1,d2 = d1.copy(),d2.copy()
    return _rec_combat(d1,d2)[1]

def _rec_combat(d1,d2):
    seen = set()

    while len(d1) > 0 and len(d2) > 0:
        m = (tuple(d1),tuple(d2))
        if(m in seen):
            return (True,d1)
        seen.add(m)

        c1,c2 = d1.pop(0),d2.pop(0)
        if len(d1) >= c1 and len(d2) >= c2:
            r,_ = _rec_combat(d1[:c1],d2[:c2])
        else:
            r = c1 > c2

        if r:
            d1 += [c1,c2]
        else:
            d2 += [c2,c1]
    
    return (len(d2) == 0,max(d1,d2))

def score(deck):
    return sum((i+1)*n for i,n in enumerate(reversed(deck)))
    
silver = score(combat(d1,d2))
gold = score(rec_combat(d1,d2))

print("silver:",silver)
print("gold:",gold)
