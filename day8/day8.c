#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

enum {ACC,JMP,NOP};
#define MAX_INSTRUCTIONS 3000000

struct state {
    int acc;
    int ip;
};

struct instr {
    int op;
    int n;
};

void step(struct state* S,struct instr* program);
void swap_step(struct state* S,struct instr* program);
void fast_solver(struct instr* program,int program_len);

void fast_solver(struct instr* program,int program_len) {
    bool* seen = calloc(program_len,sizeof(bool));
    bool* branch_seen = calloc(program_len,sizeof(bool));

    seen[program_len] = true;
    branch_seen[program_len] = true;
    bool gold_found = false;
    int gold;

    struct state S;
    struct state b_S;
    S.acc = 0;
    S.ip = 0;

    while(!gold_found) {
        seen[S.ip] = true; 
        branch_seen[S.ip] = true;
        if(program[S.ip].op == NOP || program[S.ip].op == JMP) {
            b_S.acc = S.acc;
            b_S.ip = S.ip;
            swap_step(&b_S,program);

            while(!branch_seen[b_S.ip]) {
                branch_seen[b_S.ip] = true;
                step(&b_S,program);
            }
            if(b_S.ip == program_len) {
                gold_found = true;
                gold = b_S.acc;
            }
        } 
        step(&S,program);
    }
    while(!seen[S.ip]) {
        seen[S.ip] = true;
        step(&S,program);
    }
    printf("silver: %d\ngold: %d\n",S.acc,gold);
}

void step(struct state* S,struct instr* program) {
    switch(program[S->ip].op) {
        case ACC:
            S->acc += program[S->ip].n;
            S->ip += 1;
            break;
        case JMP:
            S->ip += program[S->ip].n;
            break;
        case NOP:
            S->ip += 1;
            break;
    }
}

void swap_step(struct state* S, struct instr* program) {
    switch(program[S->ip].op) {
        case ACC:
            S->acc += program[S->ip].n;
            S->ip += 1;
            break;
        case NOP:
            S->ip += program[S->ip].n;
            break;
        case JMP:
            S->ip += 1;
            break;
    }
}

int main() {
    char* line;
    int n;
    size_t len;
    ssize_t read;
    struct instr* program = malloc(sizeof(struct instr) * MAX_INSTRUCTIONS); 

    FILE* fp = fopen("day8.input","r");
    if(fp == NULL) {
        printf("can't read input\n");
        return 1;
    }

    int i = 0;
    while((read = getline(&line,&len,fp)) != -1) {
        n = atoi(&line[4]);
        switch(line[0]) {
            case 'a':
                program[i].op = ACC;
                break;
            case 'j':
                program[i].op = JMP;
                break;
            case 'n':
                program[i].op = NOP;
                break;
        }
        program[i].n = n;
        i += 1;
    }   
    int program_len = i;
    //printf("Program length: %d\n",program_len);
    fast_solver(program,program_len);
    return 0;
}
