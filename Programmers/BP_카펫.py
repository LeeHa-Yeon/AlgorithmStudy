'''
brown	yellow	return
10	    2	    [4, 3]
8	    1	    [3, 3]
24      24  	[8, 6]
'''

from itertools import combinations_with_replacement


def solution(brown, yellow):
    divisorList = []
    perList = []
    answer = []
    a = (brown-4)//2

    for i in range(1,yellow+1) :
        if yellow%i == 0 :
            divisorList.append(i)

    if yellow == 1 :
        answer.append(3)
        answer.append(3)
    else :
        perList.append(list(combinations_with_replacement(divisorList,2)))
        print(perList)
        for i in perList[0]:
            print(i[0], i[1])
            if i[0] + i[1] == a and i[0] * i[1] == yellow:
                answer.append(i[1] + 2)
                answer.append(i[0] + 2)
    return answer

print(solution(12,4))


''' yellow가 정사각형에 가까울때
 
def solution(brown, yellow):
    divisorList = []
    answer = []

    for i in range(1,yellow+1) :
        if yellow%i == 0 :
            divisorList.append(i)

    idx = len(divisorList) // 2

    width = divisorList[idx]+2
    height = (yellow//divisorList[idx])+2

    answer.append(width)
    answer.append(height)

    return answer

print(solution(12,6))
'''