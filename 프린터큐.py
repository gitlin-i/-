import sys
class PriorityQueue:
    def __init__(self, mem,m) -> None:
        self.mem = mem
        self.print_count = 0
        self.priority_count = {i:0 for i in range(1,10)}
        self.ind = m
        for pri in self.mem:
            self.priority_count[pri] +=1
        
    def isEmpty(self):
        if len(self.mem) > 0:
            return False
        return True

    def check_Priority(self,pri):
        for i in range(pri+1,10):
            if self.priority_count[i] > 0:
                return False
        return True

    def Print_element(self):
        if not self.isEmpty():
            if self.check_Priority(self.mem[0]):
                self.priority_count[self.mem[0]] -=1
                self.print_count +=1

                if self.ind == 0:
                    return self.print_count
            else:
                self.mem.append(self.mem[0])

            
            self.mem.pop(0)
            self.ind -= 1
            if self.ind < 0:
                self.ind = len(self.mem)-1
        return False
            
    


            

input = sys.stdin.readline

case_n = int(input())
answer = []
for _ in range(case_n):
    N,M = map(int,input().split())
    priotiy_docs = list(map(int,input().split()))

    Q = PriorityQueue(priotiy_docs,M)
    a = Q.Print_element()
    while a is False:
        a = Q.Print_element()

    answer.append(a)

for a in answer:
    print(a)
    





"""
boj_problem=1966
"""