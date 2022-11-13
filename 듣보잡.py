import sys

input = sys.stdin.readline

n,m = map(int,input().split())
not_listened = []
not_seen = []

for _ in range(n):
    not_listened.append(input().rstrip())

for _ in range(m):
    not_seen.append(input().rstrip())

not_listened_and_seen = set(not_listened) & set(not_seen)

print(len(not_listened_and_seen))

temp = list(not_listened_and_seen)
temp.sort()
for t in temp:
    print(t)



"""
boj_problem=1764
"""