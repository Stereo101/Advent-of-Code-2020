from advent import Session

aoc = Session(2020,8)
with aoc.fp() as fp:
    L = [line.strip() for line in fp.readlines()]

instr = []
for line in L:
    cmd,n = line.split(" ")
    instr.append((cmd,int(n)))

def fast_sol(instr):
    ip,acc = 0,0

    seen = set()
    seen.add(len(instr))

    branch_seen = set()
    branch_seen.add(len(instr))

    gold_found = False
    gold = None
    
    #run p1 and p2
    while not gold_found:
        cmd,n = instr[ip]
        seen.add(ip)
        branch_seen.add(ip)

        #branch on jmp/nop
        if(cmd == "jmp" or cmd == "nop"):
            b_ip,b_acc = step(ip,acc,instr,swap=True)

            #stop branch if instruction has been seen 
            while b_ip not in branch_seen:
                branch_seen.add(b_ip)
                b_ip,b_acc = step(b_ip,b_acc,instr)

            if(b_ip == len(instr)):
                gold_found = True
                gold = b_acc

        ip,acc = step(ip,acc,instr)

    #finish p1
    while ip not in seen:
        cmd,n = instr[ip]
        seen.add(ip)
        ip,acc = step(ip,acc,instr)

    return acc,gold
    
swap_dict = {"acc":"acc","jmp":"nop","nop":"jmp"}
def step(ip,acc,instr,swap=False):
    cmd,n = instr[ip]
    cmd = swap_dict[cmd] if swap else cmd

    if(cmd == "acc"):
        return ip+1,acc+n
    elif(cmd == "jmp"):
        return ip+n,acc
    return ip+1,acc

silver,gold = fast_sol(instr)
print("silver:",silver,"\ngold:",gold)
