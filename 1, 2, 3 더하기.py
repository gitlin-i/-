import sys

input = sys.stdin.readline
n = int(input())
input_list = []
memo = [0] * 11
for _ in range(n):
    input_list.append(int(input()))

memo[1] = 1
memo[2] = 2
memo[3] = 4 

for i in range(4,11):
    memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        
for input in input_list:
    print(memo[input])
"""
boj_problem=9095
"""