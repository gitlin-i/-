
import sys


case_n = int(sys.stdin.readline())
x_y_list = []
for _ in range(case_n):
    x, y = map(int,sys.stdin.readline().split())
    x_y_list.append((x,y))

answer = {}
for x_y in x_y_list:
    rank = 1
    for x_y_2 in x_y_list:
        if x_y != x_y_2:
            if x_y[0] < x_y_2[0] and x_y[1] < x_y_2[1]:
                rank += 1
    
    answer[x_y] = rank




for x_y in x_y_list:
    print(answer[x_y],end= ' ')







"""
boj_problem=7568
"""
