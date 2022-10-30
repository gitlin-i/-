import sys


class Ground:
    def __init__(self,mat) -> None:
        self.matrix = mat
        
    def ground_minus_h_matrix(self,h):
        new_matrix = []
        for n in self.matrix:
            new_matrix.append([i - h for i in n])
        return new_matrix

class Actor:
    def __init__(self,b) -> None:
        self.block = b
        self.action_cost = 0
        self.notworked = False
    def remove_block(self,ground):
        for n in ground:
            for m in n:
                if m > 0:
                    self.action_cost +=  m * 2
                    self.block += m 
    def add_block(self,ground):
        for n in ground:
            for m in n:
                if m < 0:
                    if self.block >= (-1 * m):
                        self.action_cost += m * -1
                        self.block -= m
                    else:
                        self.notworked = True
                        return -1
    def work(self,ground):
        self.remove_block(ground)
        self.add_block(ground)

    def get_action_cost(self):
        if self.notworked:
            return 999

        return self.action_cost



n,m,b = map(int,sys.stdin.readline().split())
max_height = 256
cost_list = []
temp=[]
for _ in range(n):
    temp.append(list(map(int,sys.stdin.readline().split())))

ground = Ground(temp)

for h in range(max_height+1):
    lvalue = Actor(b)
    lvalue.work(ground.ground_minus_h_matrix(h))
    cost_list.append((lvalue.get_action_cost(),h))

minimum_cost = min(cost_list)

max_h = max([ i for i in range(len(cost_list)) if cost_list[i] == minimum_cost])

print(minimum_cost,max_h)





"""
boj_problem=18111
"""