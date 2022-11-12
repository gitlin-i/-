import sys
input = sys.stdin.readline

n = int(input())
total_0 = 0


n_fac = 1
for i in range(1,n+1):
    n_fac *=i

str_n_fac = str(n_fac)

for ch in str_n_fac[::-1]:
    if ch =='0':
        total_0 +=1
    else:
        break
print(total_0)
        
"""
boj_problem=1676
"""
