'''
scoville	K	return
[1, 2, 3, 9, 10, 12]	7	2
'''

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0

    # 앞자리가 데시벨보다 작을 경우
    while scoville[0] < K and len(scoville) > 1 :
        heapq.heappush(scoville, heapq.heappop(scoville) + (2 * heapq.heappop(scoville)))
        cnt += 1

    # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우
    maxValue = heapq.nlargest(1, scoville)
    if len(scoville) == 1 and maxValue[0] < K:
        cnt = -1

    return cnt

print(solution([1, 2, 3, 9, 10, 12],7))
# print(solution([1, 1, 1], 4)) # 2
# print(solution([10, 10, 10, 10, 10], 100)) # 4
# print(solution([1, 2, 3, 9, 10, 12], 7)) # 2
# print(solution([0, 2, 3, 9, 10, 12], 7)) # 2
# print(solution([0, 0, 3, 9, 10, 12], 7)) # 3
# print(solution([0, 0, 0, 0], 7))  # -1
# print(solution([0, 0, 3, 9, 10, 12], 7000))  # -1
# print(solution([0, 0, 3, 9, 10, 12], 0)) #0
# print(solution([0, 0, 3, 9, 10, 12], 1)) # 2
# print(solution([0, 0], 0))  #0
# print(solution([0, 0], 1))  # -1
# print(solution([1, 0], 1))  # 1


