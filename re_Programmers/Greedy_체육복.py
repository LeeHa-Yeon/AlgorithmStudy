'''
n	lost	reserve	return
5	[2, 4]	[1, 3, 5]	5
5	[2, 4]	[3]	4
3	[3]	[1]	2
'''

# 5, [1, 2, 3], [2, 3, 4]
def solution(n, lost, reserve):
    student = [ i for i in range(1,n+1)]
    lesson = set(student)-set(lost)
    same = []

    for i in reserve :
        if i in lost :
            same.append(i)
    lost = list(set(lost) - set(same))
    reserve = list(set(reserve) - set(same))


    while lost :
        standard = lost.pop(0)  # 1

        for i in range(len(reserve)) :
            if reserve[i]-1 == standard or reserve[i]+1 == standard:
                lesson.add(standard)
                reserve.pop(i)
                reserve.append(40)

    return len(lesson)+len(same)

# print(solution(5,	[2, 4],	[1, 3, 5]))
# print("-----")
# print(solution(5,	[2, 4]	,[3]))
# print("-----")
# print(solution(3,	[3],	[1]))
# print("-----")
# print(solution(5,	[3],	[1,3]))
# print("------")
# print(solution(2, [2], [1] ))
# print("------")
# print(solution(7 ,[1, 2, 3, 4, 5, 6, 7],[1, 2, 3]))
# print("-----")
# print(solution(4, [3, 1, 2], [2, 4, 3]))

print(solution(5, [1, 2, 3], [2, 3, 4]))