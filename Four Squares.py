import sys

input = sys.stdin.readline

n = int(input())


memo = [0] * 50001
memo[1] = 1
memo[2] = 2
memo[3] = 3

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23  
# 1 2 3 1 2 3 4 2 1 2  3  3  2  3  4  1  2  2  3  2  3  3  4 

squares = [1]


for i in range(4,n+1):
    if i == (len(squares) + 1)**2:
        squares.append(i)
        memo[i] = 1
        continue
    memo[i] = memo[i-1] +1

    for j in squares:
        memo[i] = min(memo[i], memo[i-j] + memo[j])


print(memo[n])



"""
boj_problem=17626
"""


def four(n):



    if int(n**(0.5)) == n**(0.5):
        return 1

    for i in range(1,int(n**(0.5)) +1):
        if int((n- i**2)**(0.5)) == (n-i**2) ** (0.5):
            return 2
    
    for i in range(1,int(n**(0.5))+1):
        for j in range(1,int((n-i**2)**(0.5)) + 1):
            if int((n-i**2-j**2)**(0.5)) == (n-i**2-j**2) ** (0.5):
                return 4
    return 4


print('#',four(34567))