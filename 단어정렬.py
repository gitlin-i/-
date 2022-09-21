case_n = int(input())
len_sort_dict = {}
for i in range(case_n):
    input1 = input()
    if len(input1) not in len_sort_dict:
        len_sort_dict[len(input1)] = set()
    
    len_sort_dict[len(input1)].add(input1) 



len_sort_dict_keys = list(len_sort_dict.keys())
len_sort_dict_keys.sort()
for i in len_sort_dict_keys:
    alphabet_sort_list = list(len_sort_dict[i])
    alphabet_sort_list.sort()
    for j in alphabet_sort_list:
        print(j)





"""
boj_problem=1181
"""