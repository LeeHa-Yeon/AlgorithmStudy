import heapq as hq
import sys
INF = int(1e9)

v,e = map(int,sys.stdin.readline().split(" "))

start_node = int(sys.stdin.readline())
distance = [INF]*(v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e) :
    start,end,cost = map(int,sys.stdin.readline().split(" "))
    graph[start].append([end,cost])

# 다익스트라 시작
queue = []
distance[start_node] = 0
hq.heappush(queue,(distance[start_node],start_node))
while queue :
    current_distance,current = hq.heappop(queue)
    if distance[current] < current_distance :
        continue
    for adj_node,adj_cost in graph[current] :
        current_cost = current_distance +adj_cost
        if current_cost < distance[adj_node] :
            distance[adj_node] = current_cost
            hq.heappush(queue, (distance[adj_node], adj_node))

for dist in distance[1:] :
    if dist == INF :
        print("INF")
        continue
    print(dist)