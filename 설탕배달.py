import sys

def sugar(n):
    for x1 in range(1668):
        if n < x1*3: 
            break


        for x2 in range(1000+1):
            if n < x2 *5: 
                break

            if 3*x1 + 5*x2 == n:
                return x1 + x2

    return -1

n = int(sys.stdin.readline())

print(sugar(n))




"""
boj_problem=2839
"""