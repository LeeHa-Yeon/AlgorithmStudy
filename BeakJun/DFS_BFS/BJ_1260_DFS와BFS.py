'''
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

입력
4 5 1
1 2
1 3
1 4
2 4
3 4

5 5 3
5 4
5 2
1 2
3 4
3 1

1000 1 1000
999 1000

출력
1 2 4 3
1 2 3 4

3 1 2 5 4
3 1 4 2 5

1000 999
1000 999

'''


N,M,V=map(int,input().split())

# 행렬 만들기
matrix=[[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    matrix[a][b]=matrix[b][a]=1

# 방문 정점
visit_list = [False]*(N+1)

# dfs
def dfs(V):
    visit_list[V]=True # 방문 표시
    print(V, end=' ')
    for i in range(1,N+1):
        if(visit_list[i]==0 and matrix[V][i]):
            dfs(i)
#bfs
def bfs(V):
    visit_list = [False] * (N + 1) # 초기화
    queue=[V] #들려야 할 정점 저장
    visit_list[V]=1 # 방문 표시
    while queue:
        V=queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if(visit_list[i]==0 and matrix[V][i]==1):
                queue.append(i)
                visit_list[i]=1

dfs(V)
print("")
bfs(V)
