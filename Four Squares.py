import sys


input = sys.stdin.readline

n = int(input())

memo = [0] * 50001
memo[1] = 1
memo[2] = 2
memo[3] = 3

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23  
# 1 2 3 1 2 3 4 2 1 2  3  3  2  3  4  1  2  2  3  2  3  3  4 
for i in range(1,224):
    memo[i*i] =1 

a = [1,2]
for i in range(4,50001):
    if (a[-1] +1) **2 < i:
        a.append(a[-1] +1)

    for j in a:
        memo[i] = min(memo[i-1]+1 , memo[i-j] + memo[j])

print(memo[n])



"""
boj_problem=17626
"""