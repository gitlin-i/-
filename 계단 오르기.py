import sys
input = sys.stdin.readline

n = int(input().rstrip())
steps = [0]
cost = [0] * (n+1)



for _ in range(n):
    k = int(input().rstrip())
    steps.append(k)


cost[1] += steps[1]
if n >= 2:
    cost[2] += steps[1] + steps[2]
    if n>=3:
        cost[3] = max(steps[1] + steps[3], steps[2] + steps[3])

        for i in range(4,n+1):

            cost[i] = max(cost[i-2]+ steps[i], cost[i-3] + steps[i-1] + steps[i])

print(cost[n])


"""
boj_problem=2579
"""