import sys
input = sys.stdin.readline

class Stack:
    def __init__(self) -> None:
        self.mem = []
        self.answer = []
    def empty(self):
        if len(self.mem)>0:
            return False
        return True

    def push(self, x):
        self.mem.append(x)
        self.answer.append('+')

    def pop(self):
        if not self.empty():
            self.answer.append('-')
            return self.mem.pop()
        return -1

    def top(self):
        if not self.empty():
            return self.mem[-1]
        return -1

    def stack_seq(self,seq):
        seq_ind =0
        pop_seq = []
        for i in range(1,len(seq)+1):
            if self.top() != seq[seq_ind]:
                self.push(i)
            else:
                while self.top() == seq[seq_ind]:
                    pop_seq.append(self.pop())
                    seq_ind += 1

                self.push(i)
        #계속 집어넣다가 수가 겹치면 중간에 pop
        
        while not self.empty():
            pop_seq.append(self.pop())
            seq_ind += 1
        #나머지 수 출력

        for i in range(len(pop_seq)-1,-1,-1):
            if pop_seq[i] != seq[i]:
                self.answer = ['NO']
                return 
        #출력한 문자열하고 원본하고 비교
                
    def getAnswer(self):
        return self.answer

n = int(input())
seq = []
for _ in range(n):
    seq.append(int(input()))

stack =Stack()
stack.stack_seq(seq)
answer = stack.getAnswer()
for a in answer:
    print(a)


"""
boj_problem=1874
"""
