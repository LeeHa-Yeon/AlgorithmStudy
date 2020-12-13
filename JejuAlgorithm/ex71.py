# 깊이 우선 탐색 depth first search
# : bfs와 다른 점 : queue대신 stack을 사용
# : 하나의 노드에서 시작하여 마지막 지점까지 계속 탐색하는 행동을 하는 알고리즘인데
#   즉, 시작점을 기준으로 가장 아래까지 이동하면서 탐색하는 방식



graph = {
    'E' : ['D','A'],
    'D' : ['E','F'],
    'F' : ['D'],
    'A' : ['E','C','B'],
    'C' : ['A'],
    'B' : ['A']
}

graph2 = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D'],
        'D': ['C', 'E', 'G'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
    }


def dfs_left(graph, start):
    visited = list()
    stack = list()

    stack.append(start)

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            # reversed하면 왼쪽 깊이우선탐색
            stack.extend(reversed(graph[node]))

    return visited


def dfs_right(graph, start):
    visited = list()
    stack = list()

    stack.append(start)

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            # reversed 없으면 오른쪽 깊이우선탐색
            stack.extend(graph[node])

    return visited

print(dfs_left(graph, 'E'))
# ['E', 'D', 'F', 'A', 'C', 'B']

print(dfs_right(graph, 'E'))
# ['E', 'A', 'B', 'C', 'D', 'F']


'''
- append, extend 차이 - 
list.append(x)는 리스트 끝에 x 1개를 넣습니다.
list.extend(iterable)는 리스트 끝에 iterable의 모든 항목을 넣습니다.

if x가 문자열일 경우엔
append는 x 그 자체를 원소로 넣고 extend는 문자열의 각 알파벳을 넣습니다

'''


'''
0번째 current : E
0번째 visited : ['E']
0번째 stack : ['A', 'D']

1번째 current : D
1번째 visited : ['E', 'D']
1번째 stack : ['A', 'F', 'E']

2번째 current : E
2번째 current : F
2번째 visited : ['E', 'D', 'F']
2번째 stack : ['A', 'D']

3번째 current : D
3번째 current : A
3번째 visited : ['E', 'D', 'F', 'A']
3번째 stack : ['B', 'C', 'E']

4번째 current : E
4번째 current : C
4번째 visited : ['E', 'D', 'F', 'A', 'C']
4번째 stack : ['B', 'A']

5번째 current : A
5번째 current : B
5번째 visited : ['E', 'D', 'F', 'A', 'C', 'B']
5번째 stack : ['A']

6번째 current : A
['E', 'D', 'F', 'A', 'C', 'B']

'''