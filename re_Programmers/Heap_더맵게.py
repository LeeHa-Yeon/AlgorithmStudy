'''
scoville	K	return
[1, 2, 3, 9, 10, 12]	7	2
'''

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0

    while scoville[0] < K and len(scoville) > 1 :
        heapq.heappush(scoville,heapq.heappop(scoville) + (2 * heapq.heappop(scoville)))
        cnt+=1

    if len(scoville) == 1 and scoville[0] < K :
        cnt = -1


    return cnt

print(solution([1, 2, 3, 9, 10, 12],7))


