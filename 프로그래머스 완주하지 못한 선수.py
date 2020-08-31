#프로그래머스 완주하지 못한 선수
#https://programmers.co.kr/learn/courses/30/lessons/42576
def tuple_g(a):
    return len(a),a[0]

def solution(participant, completion):
    dic_a={}
    for i in range(0,len(participant)):
        if tuple_g(participant[i]) not in dic_a:
            dic_a[tuple_g(participant[i])] = [participant[i]]
        else:
            dic_a[tuple_g(participant[i])].append(participant[i])
    for j in range(0,len(completion)):
        dic_a[tuple_g(completion[j])].remove(completion[j])
        if dic_a[tuple_g(completion[j])] == []:
            del dic_a[tuple_g(completion[j])]
    for key in dic_a:
        return dic_a[key][0]

#드디어 효율성테스트 통과
#1~20자이며 첫 문자를 이용해 글자수,첫글자 튜플을 딕셔너리에 리스트형태로 분류
#그 뒤 하나씩 값을 제거해 마지막에 남는 키 값을 출력