

import sys

class Stack:
    def __init__(self) -> None:
        self.mem = []
        self._top = -1

    def pop(self):

        if len(self.mem) >= 1:
            self._top -=1
            return self.mem.pop()
        else:
            return -1


    def push(self,x):
        self.mem.append(x)
        self._top += 1
        

    def size(self):
        return len(self.mem)

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def top(self):
        try:
            return self.mem[self._top]
        except:
            return -1


    def channel(self,string):
        string_ = string.split()
        
        if string_[0] == 'top':
            print(self.top())
            

        elif string_[0] == 'size':
            
            print(self.size())


        elif string_[0] == 'empty':
            print(self.empty())

        elif string_[0] == 'pop':
            print(self.pop())

        elif string_[0] == 'push':
            self.push(int(string_[1]))

oper_n = int(sys.stdin.readline())

stack = Stack()
for _ in range(oper_n):

    stack.channel(sys.stdin.readline())





"""
boj_problem=10828
"""
