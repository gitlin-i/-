#프로그래머스 완주하지 못한 선수
#https://programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion): 
    answer = participant.copy()
    for i in range(0,len(participant)):
        for j in range(0,len(completion)) :
            if participant[i] == completion[j]:
                answer.remove(completion[j])
    return answer

answer=solution(["mislab", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])[0]
print(answer)

#동명이인에 대한 처리 불가, 문제의 주제는 해시였음
#해시를 통해 다시풀어보기
#변수 = 리스트 -> 리스트 주소 값 복사
#변수 = 리스트.copy() -> 리스트 값 복사