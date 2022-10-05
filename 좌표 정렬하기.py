import sys
coord_n = int(sys.stdin.readline())
plane = {}
for _ in range(coord_n):
    coord = tuple(map(int,sys.stdin.readline().split()))
    if coord[0] not in plane:
        plane[coord[0]] = []
    plane[coord[0]].append(coord[1])

keys = list(plane.keys())
keys.sort()

for key in keys:
    now_sort_y = plane[key]
    now_sort_y.sort()
    for y in now_sort_y:
        print(key,y)


"""
boj_problem=11650
"""