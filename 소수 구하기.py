import sys

    
def prime_number(m,n):
    depth = int(n ** 0.5)
    mat = [True] * (n+1)
    mat[0] = False
    mat[1] = False
    for i in range(2,depth +1):
        if mat[i] == True:
            for j in range(2, (n // i)+1):
                mat[i*j] = False
    
    return [ i for i in range(m,n+1) if mat[i] == True]



M, N = map(int,sys.stdin.readline().split())
for p in prime_number(M,N):
    print(p)



"""
boj_problem=1929
"""