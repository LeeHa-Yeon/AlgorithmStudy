'''
N	road	K	result
5	[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]	3	4
6	[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]	4	4
'''

import heapq as h

INF = int(1e9)

def solution(N, road, K):
    distance = [INF] * (N + 1)
    q = []

    # 모든 간선 정보를 입력받기
    road.sort()
    graph = [[] for _ in range(N + 1)]
    for i in road:
        graph[i[0]].append((i[1], i[2]))

    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    h.heappush(q, (1, 0))
    distance[1] = 0

    while q:  # 큐가 비어있지 않다면
        print(q)
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        now, dist = h.heappop(q)
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            print(i)
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost > K:
                distance[i[0]] = cost
                h.heappush(q, (cost, i[0]))
    return

print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))
