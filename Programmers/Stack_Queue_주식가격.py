'''
prices	        return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]

'''

from collections import deque

def solution(prices):
    dp = deque(prices)
    result = []

    while dp :
        cnt = 0
        num = dp.popleft()
        for i in dp:
            cnt += 1
            if num > i:
                break
        result.append(cnt)

    return result


print(solution([ 1, 2, 3, 2, 3, 1 ]))



''' 정확성 100 / 효율성 0 -> 시간초과 
def solution(prices):
    stack = []

    while prices :
        cnt = 0
        num = prices.pop(0)
        for i in prices :
            cnt += 1
            if num > i :
                break
        stack.append(cnt)

    return stack


print(solution([1, 2, 3, 2, 3]))  

'''