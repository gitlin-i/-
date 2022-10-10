import sys

n, m  = map(int, sys.stdin.readline().split())

trees = list(map(int, sys.stdin.readline().split()))

start , end = 1, 1000000000

while start <= end:
    count = 0 
    h = (start + end) // 2

    for tree in trees:
        if tree > h:
            count += tree - h
            if count >= m: break

    if count < m:
        end = h - 1
    
    else:
        start = h +1

print(end)




"""
boj_problem=2805
"""