import heapq

nums = [4, 1, 7, 3]
heap = []

for num in nums:
    heapq.heappush(heap, num)  # (우선 순위, 값)
print(heap)



