import sys


class CircleQueue:
    def __init__(self,n,k) -> None:
        
        self.n = n
        self.k = k
        self._ind = -1
        self.mem = [i for i in range(1,self.n+1)]
    def index_check(self):
        while self._ind >= len(self.mem):
            self._ind -= len(self.mem)
    def next(self):
        self._ind += self.k
        self.index_check()

    def index_correction(self):
        if not self._ind == 0 :
            self._ind -=1
        else:
            self._ind = len(self.mem) -1 

    def one_pop(self):
        self.next()

        temp = self.mem.pop(self._ind)

        self.index_correction()
        return temp



n,k = map(int,sys.stdin.readline().split())

a = CircleQueue(n,k)
answer = []
for i in range(a.n):
    answer.append(a.one_pop())

print('<{}>'.format(answer).replace('[','').replace(']',''))
"""
boj_problem=11866
"""