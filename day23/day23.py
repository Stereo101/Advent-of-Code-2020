from advent import Session
aoc = Session(2020,23)

#with aoc.fp() as fp:
#    cups = [int(x) for x in fp.read().strip()]
cups = [int(c) for c in "598162734"]

def make_network(G,size):
    #By default next(index) -> index+1
    d = list(range(1,(size+1)+1))
    root = G[0]
    last = root
    for x in G[1:]:
        d[last] = x
        last = x
    if(len(G) == size):
        d[last] = root
    else:
        d[last] = len(G)+1
        d[size] = root
    return root,d

def play(root,d,moves):
    smallest = 1
    biggest = len(d)-1
    current = root
    move = 0
    while move < moves:
        sel_head = d[current]
        sel_mid = d[sel_head]
        sel_tail = d[sel_mid]
        next_node = d[sel_tail]
        dest = current-1
        while dest == sel_head or dest == sel_mid or dest == sel_tail or dest < smallest:
            dest = dest-1
            if(dest < smallest):
                dest = biggest 
        d[dest],d[sel_tail] = sel_head,d[dest]
        d[current] = next_node
        current = next_node
        move += 1

#cups = [int(x) for x in "389125467"]
root,d = make_network(cups,len(cups)) 
play(root,d,100)
silver = []
cur = d[1]
while cur != 1:
    silver.append(str(cur))
    cur = d[cur]
print("silver:","".join(silver))

root,d = make_network(cups,1000000)
play(root,d,10000000)
gold = d[1] * d[d[1]]
print("gold:",gold)
