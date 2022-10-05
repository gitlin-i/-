import sys
import math
A,B,V = map(int,sys.stdin.readline().split())

d = 1
V -= A
d2 = math.ceil(V /(A-B))
print(d+ d2)


"""
boj_problem=2869
"""