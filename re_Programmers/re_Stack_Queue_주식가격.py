'''
prices	return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
'''

from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)

    while prices :
        p = prices.popleft()
        cnt = 0
        for price in prices:
            cnt += 1
            if p > price:
                break
        answer.append(cnt)

    return answer

print(solution([1, 2, 3, 2, 3]))