# 최단 경로 찾기
# 다음과 같은 노드의 연결 관계가 그래프 형태로 주어집니다.
# 그 다음 경로를 구할 두 정점이 공백으로 구분되어 주어질 것입니다.
# 두 정점 사이를 이동할 수 있는 최단거리를 출력하는 프로그램을 작성해 주세요.
# 이 때 최단거리란, 정점의 중복 없이 한 정점에서 다른 정점까지 갈 수 있는 가장 적은 간선의 수를 의미
#

graph={
    'A': set(['B','C']),
    'B': set(['A','D','E']),
    'C': set(['A','F']),
    'D': set(['B']),
    'E': set(['B','F']),
    'F': set(['C','E'])
}

def bfs(graph,startNode,endNode):
    queue = [startNode]
    visited = [startNode]
    distance = -1

    while queue:

        distance += 1

        for i in range(len(queue)):
            current_node = queue.pop(0)
            # print(current_node,distance)
            if current_node == endNode:
                return distance
            for next_node in graph[current_node]:
                if next_node not in visited:
                    queue.append(next_node)
                    visited.append(next_node)
    return distance

userInput1='A' ; userInput2='F'

print("{} 와 {} 사이의 최단 distance :".format(userInput1,userInput2),bfs(graph,userInput1,userInput2))




