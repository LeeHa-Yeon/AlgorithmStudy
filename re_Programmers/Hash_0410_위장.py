'''
clothes	return
[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]	5
[["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]	3
'''

'''
< 키가 겹치는 두개의 dict를 합치는 방법  : Counter >

Counter는 컨테이너에 동일한 값의 자료가 몇개인지를 파악하는데 사용하는 객체

1. collections.Counter를 쓰는 방법 - dict의 value가 숫자인 경우
[collections.Counter]는 dict의 하위 클래스로, key와 key의 count값을 key-value 쌍으로 저장해 줍니다. *다만, dict의 value가 숫자인 경우만 쓸 수 있습니다

2. 

링크 : https://excelsior-cjh.tistory.com/94

'''

import collections

def solution(clothes) :
    clothesDict = dict(clothes)
    clothesCnt = collections.Counter(clothesDict.values())
    answer = 1

    for k, v in clothesCnt.items():
        answer *= (v+1)

    return answer-1

print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))