
import sys

class Stack:

    def __init__(self) -> None:
        self.mem = []
    def pop(self, x=None):
        if x is None:
            x = len(self.mem) -1

        return self.mem.pop(x)

    def check(self):
        if len(self.mem) >= 2:
            if self.mem[-2:] == ['(',')'] or self.mem[-2:] == ['[',']']:
                self.pop()
                self.pop()



    def push(self,x:None):
        
        if x in ['(','[',')',']']:
            self.mem.append(x)
            self.check()

        elif x in ('.'):
            print(self.isbalanced())
            self.flush()

        

    def isbalanced(self):
        if len(self.mem) > 0:
            return 'no'
    
        return 'yes' 
    
    def flush(self):
        self.mem.clear()




a = Stack()

while 1:
    line = sys.stdin.readline()
    if line == '.\n':
        break
    else:
        for char in line:
            a.push(char)
            


"""
boj_problem=4949
"""