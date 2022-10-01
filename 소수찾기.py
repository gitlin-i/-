def isprime(num):
    if num == 0 or num == 1: return False
    for i in range(num -1 ,1,-1):
        if num % i == 0:
            return False
    return True

case_n = int(input())
a = map(int,input().split())
count = 0
for i in a:
    if isprime(i):
        count+=1
print(count)


"""
boj_problem=1978
"""