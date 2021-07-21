'''
works	n	result
[4, 3, 3]	4	12
[2, 1, 2]	1	6
[1,1]	3	0
'''

import heapq

# def inverse(num):
#     return -num

def solution(n, works):
    answer = 0
    max_heap = list(map(lambda x : -x, works))
    # max_heap = list(map(inverse, works))
    heapq.heapify(max_heap)

    for _ in range(n):
        work = heapq.heappop(max_heap) + 1
        heapq.heappush(max_heap, work)
    if sum(max_heap) >= 0:
        return 0

    for work in max_heap:
        answer += (work ** 2)

    return answer

print(solution([4, 3, 3],4))