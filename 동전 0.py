import sys

input = sys.stdin.readline

n,k = map(int,input().split())

coins = []
count = 0
for _ in range(n):
    coins.append(int(input().rstrip()))

for coin in coins[::-1]:
    while k >= coin:
        count +=k // coin
        k %= coin



print(count)


"""
boj_problem=11047
"""