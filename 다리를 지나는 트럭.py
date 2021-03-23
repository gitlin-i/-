#프로그래머스 다리를 지나는 트럭
#https://programmers.co.kr/learn/courses/30/lessons/42583?language=python3

def list_sum(list_a):
    #현재 다리 위에 존재하는 트럭무게의 합을 반환
    sum_a = 0
    if (len(list_a) == 0):
        return 0
    for i in range(0,len(list_a)):
        sum_a += list_a[i][0]
    return sum_a

def solution(bridge_length, weight, truck_weights):
    real_time = 0
    on_bridge = []
    i = 0
    count = 0
    truck_count = len(truck_weights)
    #[트럭무게,경과시간]으로 구성
    while 1:
        #탈출하는 트럭 검사
        for j in range(0,len(on_bridge)):
            if (on_bridge[j][1] +1 > bridge_length):
                del on_bridge[j]
                count += 1
                break
        #시간 경과1
        real_time += 1
        if (count == truck_count):
            return real_time

        for k in range(0,len(on_bridge)):
            on_bridge[k][1] += 1
        #다리위에 트럭을 추가할 것인가?
        on_bridge_truck_sum = list_sum(on_bridge)
        if (i>=0 and i< truck_count):
            if (on_bridge_truck_sum + truck_weights[i] <=weight):
                on_bridge.append([truck_weights[i],1])
                i += 1

#프로그래머스 제출 완료
#특정테스트에서 994ms를 기록 -> 추가 개선방향이 필요해 보임
#스택 과 큐에 관한 문제였는데 그 개념을 이용한 느낌이 안듬...