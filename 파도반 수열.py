import sys
input = sys.stdin.readline

mem = [0] * 101

mem[1] = 1
mem[2] = 1
mem[3] = 1

for i in range(4,101):
    mem[i] = mem[i-2] + mem[i-3]

T = int(input())
for _ in range(T):
    x = int(input())
    print(mem[x])




"""
boj_problem=9461
"""