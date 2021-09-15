'''
numbers	result
[1,2,3,4,6,7,8,0]	14
[5,8,4,0,6,7,9]	6
'''


def solution(numbers):
    answer = 0

    for i in range(0 ,10) :
        if i not in numbers :
            answer+=i
    return answer

print(solution([1,2,3,4,6,7,8,0]))