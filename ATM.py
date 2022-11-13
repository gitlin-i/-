import sys

input = sys.stdin.readline

n = int(input())
ATM = list(map(int, input().split() ))
ATM.sort()
total = 0
for i in range(n):
    total += ATM[i]
    wait = 0
    for j in range(n):
        if i > j:
            wait += ATM[j]
    total += wait

print(total)






"""
boj_problem=11399
"""