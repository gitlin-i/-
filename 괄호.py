class Stack:
    def __init__(self) -> None:
        self.mem = []
        self.top = -1
    def vps_check(self):
        try:
            if (self.mem[self.top -1],self.mem[self.top]) == ('(',')'):
                return True
            return False
        except Exception as e:
            print(e)
    def push(self,ch):
        self.mem.append(ch)
        self.top = len(self.mem) -1
    def pop(self):
        try:
            del self.mem[-1]
            self.top = len(self.mem) -1
        except Exception:
            self.top = -1


n = int(input())
answer = []
for _ in range(n):
    stack = Stack()
    input1 = input()

    for ch in input1:
        stack.push(ch)
        if len(stack.mem) >= 2:
            if stack.vps_check():
                stack.pop()
                stack.pop()
    
    if len(stack.mem) == 0:
        answer.append('YES')
    else:
        answer.append('NO')

for a in answer:
    print(a)


"""
boj_problem=9012
"""