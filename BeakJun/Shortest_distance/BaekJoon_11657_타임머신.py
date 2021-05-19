import sys, collections
# 무한을 의미하는 값
INF = float('inf')
g = collections.defaultdict(list)
# 노드의 개수 및 간선의 개수를 입력받기
n, m = map(int, sys.stdin.readline().split())

# 간선의 개수만큼 가중치도 있으니까 m만큼 for문 돌리기
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    g[a].append([b, c])


def bellman_ford(start):
    # 처음에 무한으로 초기화 시켜주기
    dist = [INF] * (n+1)
    dist[start] = 0
    # 최대간선의수인 n-1만큼 돌리
    for _ in range(n-1):
        # 정점 수만큼 반복
        for u in range(1, n+1):
            # 시작정점u , 도착정점 v, 가중치 c
            for v, c in g[u]:
                # 이전 값보다 작으면 갱신
                if dist[v] > dist[u] + c:
                    dist[v] = dist[u] + c
    # 한번 더 돌렸을때 값이 갱신되는 곳이 있다면 음수 사이클이 있는 것이므로 False
    for u in range(1, n+1):
        for v, c in g[u]:
            if dist[v] > dist[u] + c:
                return False
    # 갱신되는 것이 없이 온전히 끝났다면 dist 반환
    return dist

# 시작정점을 1로 설정
dist = bellman_ford(1)

if dist == False:
    print(-1)
else:
    for i in range(2, n+1):
        print(dist[i] if dist[i] < INF else -1)
