'''
n	s	a	b	fares	result
6	4	6	2	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]	82
7	3	4	1	[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]	14
6	4	5	6	[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]	18
'''


import heapq as hq
INF = int(1e9)

def dijkstra(distances, start, graph) :
    queue = []
    distances[start] = 0
    hq.heappush(queue, (distances[start], start))
    while queue:
        current_distance, current = hq.heappop(queue)
        if distances[current] < current_distance :
            continue
        for adj_node, next_distance in graph[current] :
            cost = current_distance + next_distance
            if cost < distances[adj_node] :
                distances[adj_node] = cost
                hq.heappush(queue,(distances[adj_node],adj_node))


def solution(n, s, a, b, fares):
    answer = INF
    graph = [[] for _ in range(n+1)]
    for fare in fares :
        x,y,z = fare
        graph[x].append((y,z))
        graph[y].append((x,z))

    distance = [INF]*(n+1)
    dijkstra(distance,s,graph)

    for i in range(1,n+1) :
        route = [INF]*(n+1)
        dijkstra(route,i,graph)
        answer = min(answer, distance[i] + route[a] + route[b])

    return answer

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))