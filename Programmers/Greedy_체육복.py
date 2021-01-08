def solution(n, lost, reserve):
    lost_del = set(lost)-set(reserve)
    reserve_del = set(reserve)-set(lost)

    for i in reserve_del :
        if i-1 in lost_del :
            lost_del.remove(i-1)
        elif i+1 in lost_del :
            lost_del.remove(i+1)

    return n-len(lost_del)


print(solution(5,[3],[1,3]))


'''
전체 학생의 수 n, 
체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 
여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 
체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 
이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 
남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
'''


