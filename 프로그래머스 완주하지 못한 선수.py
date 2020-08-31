#프로그래머스 완주하지 못한 선수
#https://programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    dic_a = {}
    for i in range(0,len(participant)):
        if ord(participant[i][0]) not in dic_a:
            dic_a[ord(participant[i][0])]= [participant[i]]
        else:
            dic_a[ord(participant[i][0])].append(participant[i])
    for j in range(0,len(completion)):
        dic_a[ord(completion[j][0])].remove(completion[j])
    for k in range(ord('a'),ord('z')+1):
        if k in dic_a:
            if len(dic_a[k]) == 1:
                return dic_a[k][0]

a=solution(['mislav', 'stanko', 'mislav', 'ana'],['stanko', 'ana', 'mislav'])
print(a)

#첫번째 반복문으로 이름 첫글자로 키값을 정하고 첫글자가 같은 이름들을 리스트 형태로 넣어 딕셔너리값을 넣음
#두번째 반복문으로 이름들을 지워나가면 키는 있으나 빈리스트와 이름 하나만 존재하는 리스트가 남겨짐
#세번째 반복문으로 키가 존재하면서 리스트 길이가 1인 값을 찾아내 반환