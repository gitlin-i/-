
class BinomialCoefficient:
    def __init__(self,N,k) -> None:
        self.N = N
        self.k = k 
    def fac(self,n):
        cumulative_product = 1
        for i in range(1, n + 1):
            cumulative_product *= i
        return cumulative_product
    
    def get(self):
        return self.fac(self.N) // (self.fac(self.N-self.k) * self.fac(self.k))

n,k = map(int,input().split())

a = BinomialCoefficient(n,k)
print(a.get())
"""
boj_problem=11050
"""
