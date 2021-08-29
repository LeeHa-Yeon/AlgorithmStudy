import heapq as hq
import sys

def dijkstra(start,graph,end) :
    queue = []
    distance = [INF] * (N + 1)
    distance[start] = 0
    hq.heappush(queue, (distance[start], start))

    while queue:
        distance_current, current = hq.heappop(queue)
        if distance_current > distance[current]:
            continue
        for adj_node, adj_cost in graph[current]:
            current_cost = distance_current + adj_cost
            if current_cost < distance[adj_node]:
                distance[adj_node] = current_cost
                hq.heappush(queue, (distance[adj_node], adj_node))

    return distance[end]



INF = int(1e9)
N,E = map(int,sys.stdin.readline().split(" "))
graph = [[] for _ in range(N+1)]
sum = 0
l = [1]

for _ in range(E) :
    a,b,c = map(int,sys.stdin.readline().split(" "))
    graph[a].append((b,c))
    graph[b].append((a,c))

v1,v2 = map(int,sys.stdin.readline().split(" "))
l.extend([v1,v2,N])

path1 = dijkstra(1,graph,v1) + dijkstra(v1,graph,v2) + dijkstra(v2,graph,N)
path2 = dijkstra(1,graph,v2) + dijkstra(v2,graph,v1) + dijkstra(v1,graph,N)

if path1 >= INF or path2 >= INF :
    print(-1)
else :
    print(min(path1,path2))