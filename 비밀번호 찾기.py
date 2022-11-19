import sys
input = sys.stdin.readline

n,m = map(int,input().split())
password_dict = {}
for _ in range(n):
    site, password = input().split()
    password_dict[site] = password

for _ in range(m):
    site = input().rstrip()
    print(password_dict[site])





"""
boj_problem=17219
"""