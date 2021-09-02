import heapq as hq
import sys
import copy

answer= 0
INF = int(1e9)
N,M,K,X = map(int,sys.stdin.readline().split(" "))
graph = [[] for _ in range(N+1)]
#pathes = [[] for _ in range(N+1)]

for i in range(M) :
    s,e = map(int,sys.stdin.readline().split(" "))
    graph[s].append(e)


# 다익스트라 시작
queue = []
distance = [INF]*(N+1)
distance[X]=0
hq.heappush(queue,(distance[X],X))

while queue :
    current_distance, current = hq.heappop(queue)
    if current_distance > distance[current] :
        continue
    #pathes[current].append(current)
    for adj_node in graph[current] :
        current_cost = current_distance+1
        if current_cost < distance[adj_node] :
            distance[adj_node] = current_cost
            hq.heappush(queue,(distance[adj_node],adj_node))
            #pathes[adj_node] = copy.deepcopy(pathes[current])

for idx in range(1,len(distance)) :
    if distance[idx] == K :
        answer+=1
        print(idx)

if answer == 0 :
    print(-1)