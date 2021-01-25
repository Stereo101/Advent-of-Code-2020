from advent import Session

aoc = Session(2020,19)

with aoc.fp() as fp:
    L = [line.strip() for line in fp.readlines()]
silver,gold = 0,0

rules = {} 
for lineN,line in enumerate(L):
    if(line == ""):
        messages = L[lineN+1:]
        break

    n,r = line.split(": ")

    if('"' in r):
        rules[n] = r[1]
    else:
        groups = r.split(" | ")
        for i in range(len(groups)):
            groups[i] = groups[i].split(" ")
        rules[n] = groups 

def match(s,rule,rules):
    groups = rules[rule]
    for g in groups:
        partial = set()
        partial.add(s)
        next_partial = set() 
        for r in g:
            if(r == "a" or r == "b"):
                next_partial |= set(p[1:] for p in partial if p.startswith(r))
            else:
                for p in partial:
                    next_partial |= set(match(p,r,rules))
            partial = next_partial
            next_partial = set()
        yield from partial
                
 
def count_matches(rule,rules,messages):
    return sum(1 for m in messages if "" in match(m,"0",rules))

silver = count_matches("0",rules,messages)
rules["8"] = [["42"],["42","8"]]
rules["11"] = [["42","31"],["42","11","31"]]
print("silver:",silver)
gold = count_matches("0",rules,messages)
print("gold:",gold)
