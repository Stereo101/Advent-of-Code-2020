from advent import Session

aoc = Session(2020,18)

with aoc.fp() as fp:
    L = [list(c for c in line.strip() if c != " ") for line in fp.readlines()]
silver,gold = 0,0

def exec(tokens,add_first=False):
    #addition first
    if(add_first):
        newTokens = []
        i = 0
        r = None 
        lastOp = None
        while i < len(tokens):
            t = tokens[i]
            if(t == "("):
                k = i+1
                x = 1
                while x != 0:
                    if(tokens[k] == "("):
                        x += 1
                    elif(tokens[k] == ")"):
                        x -= 1
                    k += 1
                z = exec(tokens[i+1:k-1],add_first=add_first)
                if(r is None):
                    r = z
                else:
                    if(lastOp == "+"):
                        r += z
                    elif(lastOp == "*"):
                        newTokens.append(r)
                        newTokens.append("*")
                        r = z
                i=k
            elif(t == "+" or t == "*"):
                lastOp = t
                i+=1
            else:
                if(r is None):
                    r = int(t)
                else:
                    if(lastOp == "+"):
                        r += int(t)
                    elif(lastOp == "*"):
                        newTokens.append(r)
                        newTokens.append("*")
                        r = int(t)
                i+=1
        if(r is not None):
            newTokens.append(r)
        tokens = newTokens

    i = 0
    r = None 
    lastOp = None
    while i < len(tokens):
        t = tokens[i]
        if(t == "("):
            k = i+1
            x = 1
            while x != 0:
                if(tokens[k] == "("):
                    x += 1
                elif(tokens[k] == ")"):
                    x -= 1
                k += 1
            z = exec(tokens[i+1:k-1],add_first=add_first)
            if(r is None):
                r = z
            else:
                if(lastOp == "+"):
                    r += z
                elif(lastOp == "*"):
                    r *= z
            i=k
        elif(t == "+" or t == "*"):
            lastOp = t
            i+=1
        else:
            if(r is None):
                r = int(t)
            else:
                if(lastOp == "+"):
                    r += int(t)
                elif(lastOp == "*"):
                    r *= int(t)
            i+=1
    return r
            
silver = sum(exec(line) for line in L)
gold = sum(exec(line,add_first=True) for line in L)

print("silver:",silver)
print("gold:",gold)
