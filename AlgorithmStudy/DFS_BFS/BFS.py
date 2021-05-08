def BFS(graph, start_node) :
    visit = list()  # 방문했던 노드를 저장하는 리스트
    queue = list()  # 다음으로 방문할 노드의 목록

    queue.append(start_node)

    while queue :
        node = queue.pop(0)
        if node not in visit :
            visit.append(node)
            queue.extend(graph[node])

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

print(BFS(graph,'A'))