
n = int(input())
list1 = [i for i in range(1,n+1)]


while len(list1) > 1:
    temp = 0
    if len(list1) % 2 == 1:
        temp = list1[-1]
        del list1[-1]
    list1 = [ x for i,x in enumerate(list1) if i % 2 == 1]

    if temp:
        list1.insert(0,temp)

print(list1[0])


"""
boj_problem=2164
"""