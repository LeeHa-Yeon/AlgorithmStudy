'''
numbers	return
17	    3
011	    2

1. 순열로 만들어서 모든 경우의 수를 만든 후
2. set로 중복을 없앰
3. 각 원소를 int로 변환
4. 각 원소가 소수인지 판별
'''

from itertools import permutations

def prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return 0
    else:
        return 0
    return 1

def solution(numbers):
    perList = list()
    perSet = set()
    answer = 0

    for i in range(len(numbers)):
        perList.append(set(map(''.join, permutations(numbers, i + 1))))

    for i in perList:
        for j in i:
            perSet.add(int(j))

    for i in perSet:
        answer += prime(i)

    return answer

print(solution("711"))
