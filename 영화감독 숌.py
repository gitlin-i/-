
def burute_return(n):
    i = 0
    a = 666
    b = []
    while i < n:
        if '666' in str(a):
            b.append(a)
            i+=1
        a+=1
    
    return b[-1]

input1 = int(input())
p = burute_return(input1)
print(p)

"""
boj_problem=1436
"""