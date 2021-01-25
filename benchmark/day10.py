from advent import Session

aoc = Session(2020,10)

with aoc.fp() as fp:
    L = [int(line.strip()) for line in fp.readlines()]
L.sort()

silver,gold = 0,0

last = 0
one = 0
three = 1
for n in L:
    if(n == last + 1):
        one += 1
    elif(n == last+3):
        three += 1
    last = n

silver = one*three
    
def ways_constant_mem(index,L):
    memo = {}
    memo[0] = 1
    for e in L:
        memo[e] = memo.get(e-1,0) + memo.get(e-2,0) + memo.get(e-3,0)
        toDel = [key for key in memo.keys() if key+3 < e]
        for key in toDel:
            del(memo[key])
    return memo[L[index]]
         
    
gold = ways_constant_mem(len(L)-1,L)
print("silver:",silver)
print("gold:",gold)
