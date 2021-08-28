import heapq as hq
import sys

INF = int(1e9)
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1) ]
distance = [INF]*(N+1)

for i in range(M) :
    s,e,c = map(int,sys.stdin.readline().split(" "))
    graph[s].append((e,c))

start_node,end_node = map(int,sys.stdin.readline().split(" "))

# 다익스트라 시작
queue = []
distance[start_node] = 0
hq.heappush(queue,(distance[start_node],start_node))

while queue :
    current_distance,current = hq.heappop(queue)
    if distance[current] < current_distance :
        continue
    for adj_node,adj_cost in graph[current] :
        current_cost = current_distance + adj_cost
        if current_cost < distance[adj_node] :
            distance[adj_node] = current_cost
            hq.heappush(queue,(distance[adj_node],adj_node))

print(distance[end_node])