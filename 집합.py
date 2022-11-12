import sys

class mySet:
    def __init__(self) -> None:
        self.Set = set()
    
    def add(self,x):
        #if x <=20 and x>=1:

        self.Set.add(x)

    def remove(self,x):
        #if x <=20 and x>=1 :
            
        self.Set.discard(x)
    def check(self, x):
        if x in self.Set:
            return 1

        return 0
    def toggle(self,x):
        #if x <= 20 and x >= 1:
        if self.check(x):
            self.Set.discard(x)
        else:
            self.add(x)

    def all(self):
        self.Set = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

    def empty(self):
        self.Set.clear()


    def channel(self,command,x= None):
        if command =='add':
            self.add(x)
        elif command == 'remove':
            self.remove(x)
        elif command == 'check':
            print(self.check(x))
        elif command == 'toggle':
            self.toggle(x)
        elif command == 'all':
            self.all()
        elif command == 'empty':
            self.empty()





input = sys.stdin.readline

n_command = int(input())
a = mySet()

for _ in range(n_command):
    arr  = input().split()
    command = arr[0]
    x = arr[-1]

    if command != x:
        a.channel(command,int(x))
    else:
        a.channel(command)




"""
boj_problem=11723
"""