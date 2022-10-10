import sys

k, n  = map(int, sys.stdin.readline().split())
Lan_cables = []
for _ in range(k):
    Lan_cables.append(int(sys.stdin.readline()))

start , end = 1, max(Lan_cables)

while start <= end:
    count = 0 
    mid = (start + end) // 2

    for lan_cable in Lan_cables:
        count += lan_cable // mid

    if count < n:
        end = mid -1
    
    else:
        start = mid +1

print(end)




"""
boj_problem=1654
"""