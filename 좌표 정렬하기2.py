
import sys


case_n = int(sys.stdin.readline())
x_y_list = []
for _ in range(case_n):
    x, y = map(int,sys.stdin.readline().split())
    x_y_list.append((x,y))


s = sorted(x_y_list, key=lambda x:x[0])
ss = sorted(s,key= lambda y: y[1])

for x_y in ss:
    print(x_y[0],x_y[1])


"""
boj_problem=11651
"""
