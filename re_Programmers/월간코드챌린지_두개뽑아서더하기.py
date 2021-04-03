# numbers	result
# [2,1,3,4,1]	[2,3,4,5,6,7]
# [5,0,2,7]	[2,5,7,9,12]

# set, 조합, 정렬

from itertools import combinations

def solution(arr) :

    l = map(list,combinations(arr,2))
    l2 = set()

    for i in l :
        l2.add(i[0]+i[1])
    l2 = list(sorted(l2))

    return l2

print(solution([5,0,2,7]))