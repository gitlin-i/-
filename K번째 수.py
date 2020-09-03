#k번째 수
#https://programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    cut_array ={}
    answer=[]
    for p in range(0,len(commands)):
        i,j,k=commands[p][0],commands[p][1],commands[p][2]
        if (i,j) not in cut_array:
            cut_array[(i,j)]= list_cut(array,i,j)
        answer.append(cut_array[i,j][k-1])
    return answer

def list_cut(array,i,j):
    list_a = [array[q] for q in range(i-1,j)]
    list_a.sort()
    return list_a

a=solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])
print(a)


#commands 의 원소 i,j를 디렉토리에 등록해 한 번 범위를 구하고 정렬한 리스트를 재사용하려함
#정확성 테스트 성공, 효율성테스트는 존재x