'''
nums	result
[1,2,3,4]	1
[1,2,7,6,4]	4
'''

from itertools import combinations

def isPrime(num) :
    for i in range(2,num) :
        if num % i == 0 :
            return 0
    return 1


def solution(nums):
    answer = 0

    nums_combi = map(list,combinations(nums,3))
    for i in nums_combi :
        sum = 0
        for j in i :
            sum+=j
        answer+=isPrime(sum)

    return answer


print(solution([1,2,7,6,4]))