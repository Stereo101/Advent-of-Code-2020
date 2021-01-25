from advent import Session
aoc = Session(2020,25)

with aoc.fp() as fp:
    L = [x.strip() for x in fp.readlines()]

pk1 = int(L[0])
pk2 = int(L[1])

def transform(subject,loop_size):
    v = 1
    for _ in range(loop_size):
        v *= subject
        v = v % 20201227
    return v

def transform_rev(subject,target):
    v = 1
    loop_size = 0
    while v != target:
        v *= subject
        v = v % 20201227
        loop_size += 1
    return loop_size


subject = 7
pk1_loops = transform_rev(subject,pk1)
key = transform(pk2,pk1_loops)
print("silver:",key)
print("gold: Merry_Christmas!")
