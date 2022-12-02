import sys
input = sys.stdin.readline

N, M = map(int,input().split())
a = list(map(int,input().split()))

for i in range(1,N):
    a[i] = a[i-1] + a[i]



for _ in range(M):
    x1,x2 = map(int,input().split())
    if x1 == 1:
        print(a[x2-1])
    else:
        print(a[x2-1] - a[x1-2])

"""
boj_problem=11659
"""