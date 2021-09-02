import heapq as hp
import sys
INF = int(1e9)

def dijkstra(start,graph,end) :
    distance = [INF]*(N+1)
    queue =[]
    distance[start] = 0
    hp.heappush(queue,(distance[start],start))

    while queue :
        distance_current, current = hp.heappop(queue)
        if distance_current > distance[current] :
            continue
        for adj_node, adj_cost in graph[current] :
            current_cost = distance[current] + adj_cost
            if current_cost < distance[adj_node] :
                distance[adj_node] = current_cost
                hp.heappush(queue,(distance[adj_node],adj_node))
    return distance[end]


N,M,X = map(int,sys.stdin.readline().split(" "))
graph = [ [] for _ in range(N+1)]
answer= []

for _ in range(M) :
    s,e,c = map(int,sys.stdin.readline().split(" "))
    graph[s].append((e,c))

for i in range(1,N+1) :
    answer.append(dijkstra(X,graph,i)+dijkstra(i,graph,X))

print(max(answer))

