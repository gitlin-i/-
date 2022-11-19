import sys
input = sys.stdin.readline


seen_fibonacci = {
    0 : [1,0],
    1 : [0,1]
    }

input_list = []

T = int(input())
for _ in range(T):
    input_list.append(int(input().rstrip()))

max_n = max(input_list)
for i in range(2,max_n+1):
    if not i in seen_fibonacci:
        seen_fibonacci[i] = [x+y for x,y in zip(seen_fibonacci[i-1],seen_fibonacci[i-2])]

for n in input_list:
    print(*seen_fibonacci[n])


"""
boj_problem=1003
"""