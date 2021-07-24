
'''
n	edge	return
6	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	3

n : 노드의 개수
edge : 각 행 [a,b]는 a번 노드와 b번 노드 사이에 간선이 있다는 것을 의미
'''

from collections import deque
def bfs(graph,distance) :
    distance[1] = 0
    queue = deque([1])
    while queue :
        current_node = queue.popleft()
        for adj_node in graph[current_node] :
            # 1과 연관되어 있지 않고 현재까지 방문한 적이 없다면 수행
            if distance[adj_node] == -1 :
                # +1(거리 증가)한 것을 자기 노드 자리에 저장
                distance[adj_node] = distance[current_node] +1
                queue.append(adj_node)
    return distance

def solution(n, edge):
    # graph는 인접 노드 정보를 담을 배열
    graph = [[] for _ in range(n+1)]
    # 인접 노드 정보 graph 각각 저장, 간선 양방향
    for a,b in edge :
        graph[a].append(b)
        graph[b].append(a)
    print(graph)
    # distance는 1번 노드로부터의 거리를 저장할 배열
    # 처음에는 모든 노드들과의 거리를 -1(무한대)로 초기화
    distance = [-1]*(n+1)
    # 0,1(자기자신)은 필요없으니 [2:]한 결과를 distance로 지정
    distance = bfs(graph,distance)[2:]
    # 가장 먼 노드를 찾아 중복된 값을 세서 반환
    return distance.count(max(distance))

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))