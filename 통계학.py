

import sys
input = sys.stdin.readline

def avg(num_list):
    return int(round(sum(num_list) /len(num_list),0))

def middle(num_list):
    
    return num_list[len(num_list) // 2]
def mode(num_list):
    dict1 = {num:0 for num in num_list}
    for num in num_list:
        if num in dict1:
            dict1[num] +=1
    target_val = max(dict1.values())
    
    keys = [k for k,v in dict1.items() if v == target_val]
    if len(keys) < 2:
        return keys[0]

    return keys[1] 

def ran(num_list):
    return max(num_list) - min(num_list)


n = int(input())

num_list = []
for _ in range(n):
    num_list.append(int(input()))

num_list.sort()

print(avg(num_list))
print(middle(num_list))
print(mode(num_list))
print(ran(num_list))


"""
boj_problem=2108
"""