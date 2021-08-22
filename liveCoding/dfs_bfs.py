def DFS(graph, root) :
    visited = []
    stack = [root]

    while stack :
        n = stack.pop()
        if n not in visited :
            visited.append(n)
            stack+=graph[n] - set(visited)
    return visited

