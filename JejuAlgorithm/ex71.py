# 깊이 우선 탐색 depth first search

graph = {
    'E' : ['D','A'],
    'D' : ['E','F'],
    'F' : ['D'],
    'A' : ['E','C','B'],
    'C': ['A'],
    'B' : ['A']
}



def dfs(graph, start):
    visited = list()
    stack = list()

    stack.append(start)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return visited

print(dfs(graph, 'E'))