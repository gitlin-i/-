
import sys

class Deque:
    def __init__(self) -> None:
        self.mem = []
        self._back= -1
        self._front = -1
    def push_front(self,x):
        if self._front < 0:
            self._front = 0
        self._back += 1
        self.mem.insert(0,x)

    def push_back(self,x):
        if self._front < 0:
            self._front = 0
        self._back += 1
        self.mem.append(x)

    def pop_front(self):
        if self.size() > 0:
            if self.size() == 1:
                self._front = -1
            self._back -= 1
            return self.mem.pop(0)
        return -1
    def pop_back(self):
        if self.size() > 0:
            if self.size() == 1:
                self._front = -1
            self._back -= 1
            return self.mem.pop()
        return -1


                

    def size(self):
        return len(self.mem)

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.size() >= 1:
            return self.mem[self._front]
        return -1

    def back(self):
        if self.size() >= 1:
            return self.mem[self._back]
        return -1


    def channel(self,string):
        string_ = string.split()

        if string_[0] == 'size': 
            print(self.size())

        elif string_[0] == 'empty':
            print(self.empty())

        elif string_[0] == 'front':
            print(self.front())

        elif string_[0] == 'back':
            print(self.back())

        elif string_[0] == 'push_front':
            self.push_front(int(string_[1]))

        elif string_[0] == 'push_back':
            self.push_back(int(string_[1]))

        elif string_[0] == 'pop_front':
            print(self.pop_front())

        elif string_[0] == 'pop_back':
            print(self.pop_back())

oper_n = int(sys.stdin.readline())

deque1 = Deque()
for _ in range(oper_n):

    deque1.channel(sys.stdin.readline())





"""
boj_problem=10866
"""