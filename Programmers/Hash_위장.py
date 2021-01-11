'''
[[yellow_hat, headgear], [blue_sunglasses, eyewear], [green_turban, headgear]]	5
[[crow_mask, face], [blue_sunglasses, face], [smoky_makeup, face]]	3
'''

from collections import Counter

def solution(clothes):
    clothes = dict(clothes)
    typeList = dict(Counter(clothes.values()))
    answer = 1
    result = []

    for i in typeList.values() :
        result.append(i+1)  # 옷을 안입은 것까지 갯수로 추가

    for i in result :
        answer*=i


    return answer-1 # 공집합 빼주기


print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))
print(solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]))