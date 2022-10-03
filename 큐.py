import sys

class Queue:
    def __init__(self) -> None:
        self.mem = []
        self._back = -1

    def pop(self):

        if len(self.mem) >= 1:
            self._back -=1
            return self.mem.pop(0)
        else:
            return -1


    def push(self,x):
        self.mem.append(x)

        self._back += 1
                

    def size(self):
        return len(self.mem)

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.size() >=1:
            return self.mem[0]
        return -1

    def back(self):
        if self.size() >=1:
            return self.mem[self._back]
        return -1


    def channel(self,string):
        string_ = string.split()
        
        if string_[0] == 'front':
            print(self.front())
            
        elif string_[0] == 'back':
            print(self.back())

        elif string_[0] == 'size':
            
            print(self.size())

        elif string_[0] == 'empty':
            print(self.empty())

        elif string_[0] == 'pop':
            print(self.pop())

        elif string_[0] == 'push':
            self.push(int(string_[1]))

oper_n = int(sys.stdin.readline())

queue = Queue()
for _ in range(oper_n):

    queue.channel(sys.stdin.readline())


"""
boj_problem=10845
"""