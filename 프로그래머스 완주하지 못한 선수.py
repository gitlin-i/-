#프로그래머스 완주하지 못한 선수
#https://programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion): 
    answer = participant.copy()
    pre = completion.copy()
    for i in range(0,len(pre)):
        answer.remove(pre[i])
    return answer

answer=solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])[0]
print(answer)

#동명이인에 대한 처리 불가, 문제의 주제는 해시였음
#해시를 통해 다시풀어보기
#변수 = 리스트 -> 리스트 주소 값 복사
#변수 = 리스트.copy() -> 리스트 값 복사
#--------------------------
#def solution(participant, completion): 
#    for i in range(0,len(completion)):
#        participant.remove(completion[i])
#    return participant[0]
#가장 적은 라인수 하지만 해시를 이용한 풀이는 아님
#코드 제출 결과 정확성은 있지만 효율적인 풀이는 아님
#즉, 해시를 이용해야함