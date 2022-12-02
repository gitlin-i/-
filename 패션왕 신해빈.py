import sys
input = sys.stdin.readline
case_n = int(input())

for _ in range(case_n):
    wear_n = int(input())
    closet = {}

    for _ in range(wear_n):
        cloth = input().split()
        if cloth[1] not in closet:
            closet[cloth[1]] = []
        closet[cloth[1]].append(cloth[0])

    cloth_num =[]

    for cloth in closet:
        cloth_num.append(len(closet[cloth]))
    
    answer = 1

    for cloth in cloth_num:
        answer *= (cloth +1)

    answer -=1
    print(answer)


"""
boj_problem=9375
"""