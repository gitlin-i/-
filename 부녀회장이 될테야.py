class Building:
    def __init__(self,k,n) -> None:
        
        self.max_floor_number = k
        self.max_room_number = n
        self.floor = {
            0 : [i for i in range(1,self.max_room_number+1)]
        }

    def floor_update(self):
        for i in range(1,self.max_floor_number+1):
            if i in self.floor:
                continue
            self.floor[i] = [ sum(self.floor[i-1][:j+1]) for j in range(self.max_room_number)  ]
        return

    def residents(self,k,n) :
        if k not in self.floor:
            self.floor_update()
        return self.floor[k][n-1]


test_case_n = int(input())
answer = []
a = []
b = []
for i in range(test_case_n):
    a.append(int(input()))
    b.append(int(input()))

building = Building(max(a),max(b))

for i in range(test_case_n):
    print(building.residents(a[i],b[i]))        

"""
boj_problem=2775
"""





