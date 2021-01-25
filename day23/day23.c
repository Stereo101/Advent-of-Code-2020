#include <stdint.h>
#include <stdio.h>

uint32_t init(uint32_t*,uint32_t*,uint32_t,uint32_t);
void play(uint32_t* d,uint32_t root,uint32_t moves,uint32_t size);
void play(uint32_t* d,uint32_t root,uint32_t moves,uint32_t size) {
    uint32_t smallest = 1;
    uint32_t biggest = size;
    uint32_t current = root;
    uint32_t temp;
    uint32_t sel_head,sel_mid,sel_tail,next_node,dest;
    while (moves--) {
        sel_head = d[current];
        sel_mid = d[sel_head];
        sel_tail = d[sel_mid];
        next_node = d[sel_tail];
        dest = current-1;
        while((dest == sel_head) || (dest == sel_mid) || (dest == sel_tail) || (dest < smallest)) {
            if(dest < smallest){
                dest = biggest; 
            } else {
                dest -= 1;
            }
        }
        temp = d[dest];
        d[dest] = sel_head;
        d[sel_tail] = temp;
        d[current] = next_node;
        current = next_node;
    }
}

uint32_t init(uint32_t* d, uint32_t* input, uint32_t input_size, uint32_t size) {
    uint32_t root;
    uint32_t last;

    for(int i=1;i<=size;i++) {
        d[i] = i+1;
    }
    root = input[0];
    last = root;
    for(int i=1;i<input_size;i++) {
        d[last] = input[i];
        last = input[i];
    }
    if(input_size == size){
        d[last] = root;
    }else{
        d[last] = input_size+1;
        d[size] = root;
    }
    return root;
}

int main() {
    const uint32_t p1_size = 9;
    const uint32_t p2_size = 1000000;
    const uint32_t input_size = 9;
    static uint32_t input[] = {5,9,8,1,6,2,7,3,4};

    uint32_t p1_root;
    uint32_t p2_root;

    uint32_t p1[p1_size+1];
    uint32_t p2[p2_size+1];

    //init p2
    p1_root = init(p1,input,input_size,p1_size);
    p2_root = init(p2,input,input_size,p2_size);
    
    play(p1,p1_root,100,p1_size);
    uint32_t cur = p1[1];
    printf("silver: ");
    uint32_t silver = 0;
    while(cur != 1) {
        silver = silver * 10 + cur;
        cur = p1[cur];
    }

    play(p2,p2_root,10000000,p2_size);
    uint64_t gold = p2[1]; 
    gold *= p2[p2[1]];
    printf("silver: %d\ngold: %llu\n",silver,gold);
}
