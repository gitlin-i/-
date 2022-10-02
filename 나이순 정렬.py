import sys
sys.stdin.readline
n = int(sys.stdin.readline())
dict1 = {}
for key in range(n):
    temp = sys.stdin.readline().split()
    temp[0] = int(temp[0])

    if not temp[0] in dict1:
        dict1[temp[0]] = []
    
    dict1[temp[0]].append(temp[1])

sorted_keys =list(dict1.keys())
sorted_keys.sort()
for key in sorted_keys:  
    for name in dict1[key]:
        print(key,name)





"""
boj_problem=10814
"""












"""
boj_problem=10814
"""

