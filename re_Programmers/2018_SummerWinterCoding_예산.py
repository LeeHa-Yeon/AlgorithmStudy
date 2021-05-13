'''
d	budget	result
[1,3,2,5,4]	9	3
[2,2,3,3]	10	4
'''


def solution(d, budget):
    d.sort()
    answer = []

    for i in d :
        if budget - i >= 0 :
            budget -= i
            answer.append(i)

    return len(answer)

print(solution([1,3,2,5,4],9))
print(solution([2,2,3,3],10))