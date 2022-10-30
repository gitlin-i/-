import sys



case_n = int(sys.stdin.readline())
stack = []
for _ in range(case_n):
    input1 = int(sys.stdin.readline())

    if input1 != 0:
        stack.append(input1)
    else:
        stack.pop()

print(sum(stack))



"""
boj_problem=10773
"""