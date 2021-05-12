'''
expression	result
"100-200*300-500+20"	60420
"50*6-3*2"	300
'''

import re
from itertools import permutations
from collections import Counter

def calculation(x,op,y) :
    if op == '+' :
        return x+y
    elif op == '-' :
        return x-y
    return x*y

def solution(expression):
    answer = []
    operatorList = Counter(''.join(re.findall("\D", expression)))
    priorities = list(permutations(set(operatorList), len(set(operatorList))))

    while priorities :
        # 숫자와 문자를 구분하여 담은 리스트
        whole = re.findall("\d+|\D", expression)
        # 연산자 우선순위를 정했음
        selection = list(priorities.pop())
        # 중복 연산자를 우선순위에 맞춰 해당 연산자가 있는 위치에 삽입
        for k, v in operatorList.items():
            if v > 1:
                for _ in range(v - 1):
                    idx = selection.index(k)
                    selection.insert(idx,k)
        # 연산하는 과정
        while selection :
            # 연산자 하나를 선택
            sel = selection.pop(0)
            # 해당 위치의 인덱스를 찾아 앞뒤 숫자를 알아내기
            idx = whole.index(sel)
            a =  int(whole[idx-1])
            op = whole[idx]
            b = int(whole[idx+1])
            # 계산 후 연산자 자리에 결과값 넣고 사용한 피연산자는 없애기
            whole[idx] = calculation(a,op,b)
            del whole[idx+1]
            del whole[idx-1]
        # 최종 답을 출력하여 절댓값을 붙이고 answer에 넣기
        answer.append(abs(whole.pop()))

    # 최대값 리턴
    return max(answer)

print(solution('100-200*300-500+20'))
print(solution("50*6-3*2"))

