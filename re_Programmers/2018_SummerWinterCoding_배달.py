'''
N	road	K	result
5	[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]	3	4
6	[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]	4	4
'''

import heapq as h
INF = int(1e9)
def dijkstra(dis,graph):
    heap = []
    h.heappush(heap,[0,1])

    while heap :
        cost,node=h.heappop(heap)
        for c,n in graph[node] :
            if cost+c<dis[n] :
                dis[n]=cost+c
                h.heappush(heap,[cost+c,n])

def solution(N, road, K):
    dis = [INF]*(N+1)
    dis[1]=0
    graph = [[] for _ in range(N+1)]
    for r in road :
        graph[r[0]].append([r[2],r[1]])
        graph[r[1]].append([r[2],r[0]])
    dijkstra(dis,graph)
    return len([x for x in dis if x <=K ])



print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))
