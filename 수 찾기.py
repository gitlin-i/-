import sys

input_n = sys.stdin.readline()
a = {}
for i in map(int,sys.stdin.readline().split()):
    if i not in a:
        a[i] = 1

input_m = sys.stdin.readline()
input_Am = map(int,sys.stdin.readline().split())

for m in input_Am:
    if m in a:
        print(a[m])
    else:
        print(0)


"""
boj_problem=1920
"""