from collections import deque

def BFS(graph,start) :
    visited = []
    queue = deque(start)

    while queue :
        node = queue.popleft()
        if node not in visited :
            visited.append(node)
            queue.extend(graph[node])

    return visited

def DFS(graph,start) :
    visited = []
    stack = [start]

    while stack :
        node = stack.pop()
        if node not in visited :
            visited.append(node)
            stack.extend(graph[node])

    return visited

if __name__ == "__main__":
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

    print(BFS(graph, 'A'))
    print(DFS(graph, 'A'))
