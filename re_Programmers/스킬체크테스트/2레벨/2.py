import heapq

def solution(scoville, K):
    cnt = 0

    while cnt < scoville[-1]:
        hSort = []
        for _ in range(len(scoville)):
            hSort.append(heapq.heappop(scoville))
        heapq.heapify(hSort)
        first = heapq.heappop(hSort)
        second = heapq.heappop(hSort)
        heapq.heappush(hSort,(first+(second*2)))
        scoville = hSort
        cnt+=1
        if scoville[0] >= K :
            break

    return cnt

print(solution([1, 2, 3, 9, 10, 12],7))