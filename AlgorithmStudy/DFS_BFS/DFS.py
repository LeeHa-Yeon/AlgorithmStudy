
# stack 사용
def DFS(graph, start_node) :
    visit = list()  # 방문했던 노드를 저장하는 리스트
    stack = list()  # 다음으로 방문할 노드의 리스트

    stack.append(start_node)

    while stack :
        node = stack.pop()
        if node not in visit :
            visit.append(node)
            stack.extend(graph[node])
    return visit

graph = {
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

print(DFS(graph,'A'))