import sys
input = sys.stdin.readline

n = int(input())

n_couple = int(input())

visted = [0] * 101
stack = [1]
network = []
node = 1
visted[node] = 1
collect = []
for _ in range(n_couple):
    n1,n2 = map(int,input().split())
    network.append((n1,n2))


while len(stack) > 0:

    for net in network:
        if node in net:
            ind = 1 - net.index(node)
            stack.append(net[ind])
            collect.append(net)
    
    node = stack.pop()
    visted[node] = 1

    for col in collect:
        network.remove(col)
    collect.clear()
    
print(sum(visted)-1)



"""
boj_problem=2606
"""