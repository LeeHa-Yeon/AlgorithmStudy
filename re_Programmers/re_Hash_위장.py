'''
clothes	return
[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]	5
[["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]	3
'''
from collections import Counter
def solution(clothes) :
    clothesDic = dict(clothes)
    answer = 1
    for i in Counter(clothesDic.values()).items() :
        answer *= (i[1]+1)
    return answer-1


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))