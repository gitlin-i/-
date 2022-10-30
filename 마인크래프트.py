import sys
n,m,b = map(int,sys.stdin.readline().split())
ground = [0] *257
max_h = 0


height = 0
cost = 999999999


for _ in range(n):
    for h in map(int, sys.stdin.readline().split()):
        ground[h] += 1
        max_h = max(max_h, h)

for h in range(max_h,-1,-1):
    up = 0
    down = 0

    for now_h in range(257):

        if ground[now_h] and now_h > h:
            up += (now_h - h) * ground[now_h]
        elif ground[now_h] and now_h < h:
            down += (h - now_h) * ground[now_h]

    if up + b < down:
        continue


    time = 2* up + down
    if time < cost:
        cost = time
        height = h

print(cost,height)

"""
boj_problem=18111
"""