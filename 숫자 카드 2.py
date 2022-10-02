
dict1 ={}
case_n = int(input())
card_n = list(map(int,input().split()))
for card in card_n:
    if not card in dict1:
        dict1[card] = 1
    else:
        dict1[card] += 1

case_m = int(input())
card_m = list(map(int,input().split()))

answer = []

for card in card_m:
    if card in dict1:
        answer.append(dict1[card])
    else:
        answer.append(0)

for a in answer:
    print(a,end=' ')




"""
boj_problem=10816
"""