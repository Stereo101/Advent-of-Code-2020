from advent import Session
import math

aoc = Session(2020,13)

with aoc.fp() as fp:
    L = [line.strip() for line in fp.readlines()]

silver,gold = 0,0

 
t = int(L[0])
busses = L[1].split(",")
bmod = []
for bus in busses:
    if(bus == "x"):
        continue
    else:
        b = int(bus)
        bmod.append((b,b - (t%b)))
bmod.sort(key=lambda x:x[1])


bID,wait = bmod[0]
silver = bID*(wait)

i = 0
system = []
for bus in busses:
    if(bus == "x"):
        pass 
    else:
        b = int(bus)
        system.append((b-i,b))
    i+=1


#solve a*x = b (mod m) <stack overflow>
def cong(a, b, m):
    g = math.gcd(a, m)
    if b % g:
        raise ValueError("No solutions")
    a, b, m = a//g, b//g, m//g
    return pow(a, -1, m) * b % m, m


def crt(system):
    system.sort(key=lambda x:x[1],reverse=True)
    const,coeff = system[0]
    for r,mod in system[1:]:
        a,m = cong(coeff,r-const,mod)
        g = math.gcd(coeff,mod)
        coeff,const = coeff*mod,coeff*a+const 
    return const,coeff

const,coeff = crt(system)
gold = const
    
print("silver:",silver)
#aoc.solution(1,silver)
print("gold:",gold)
#aoc.solution(2,gold)
