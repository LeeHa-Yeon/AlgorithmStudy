'''
n	lost	reserve	return
5	[2, 4]	[1, 3, 5]	5
5	[2, 4]	[3]	4
3	[3]	[1]	2
'''

def solution(n, lost, reserve):
    student = [ i for i in range(1,n+1)]
    lesson = set(student)-set(lost)
    same = []

    # 여벌이 2개인데 체육복을 도난 당한 사람들 same
    for i in reserve :
        if i in lost :
            same.append(i)

    lost = list(set(lost) - set(same))
    reserve = list(set(reserve) - set(same))

    # 그 외 남은 사람들 중 여벌 옷을 자기 앞 뒤 사람에게 줄 수 있는 경
    while lost :
        standard = lost.pop(0)  # 1

        for i in range(len(reserve)) :
            if reserve[i]-1 == standard or reserve[i]+1 == standard:
                lesson.add(standard)
                reserve.pop(i)
                reserve.append(40)

    return len(lesson)+len(same)

print(solution(5, [1, 2, 3], [2, 3, 4]))