import sys

input = sys.stdin.readline


def isAdj(point,point2):
    if [point[0] + 1,point[1]] == point2:
        return True
    elif [point[0] - 1,point[1]] == point2:
        return True
    elif [point[0] ,point[1] +1] == point2:
        return True
    elif [point[0] ,point[1] -1] == point2:
        return True
    return False


T = int(input())

for _ in range(T):
    M,N,K = map(int,input().split())
    cabages =[]
    for _ in range(K):
        cabages.append(list(map(int,input().split())))
    queue = []
    count = 0 
    while len(cabages) > 0:
        count += 1
        queue.append(cabages[0])

        while len(queue) > 0:
            for cab in cabages:
                if isAdj(queue[0],cab) and not cab in queue:
                    queue.append(cab)
            cabages.remove(queue.pop(0))


    print(count)
           



"""
boj_problem=1012
"""
