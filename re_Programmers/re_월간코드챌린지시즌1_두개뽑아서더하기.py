'''
numbers	result
[2,1,3,4,1]	[2,3,4,5,6,7]
[5,0,2,7]	[2,5,7,9,12]
'''


from itertools import combinations

def solution(arr) :
    return sorted(list(set(map(sum,combinations(arr,2)))))


print(solution([2,1,3,4,1]))