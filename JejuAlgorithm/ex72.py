# 너비(폭) 우선 탐색 breadth first search
# : 1. queue와 dict를 사용
#   2. queue와 dict를 사용하지 않고 list를 사용
#   3. 가독성은 좋지만 성능면에서는 조금떨어짐
# : 하나로 시작 정점을 방문한 후 시작 정점에 인접한 모든 정점들을 우선 방문하는 방법이다.
#   더 이상 방문하지 않은 정점이 없을 때까지 방문하지 않은 모든 정점들에 대해서도 너비 우선 검색을 적용한다.

from queue import Queue

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
def bfs(graph,start) :
    visited = list()
    queue = list()

    queue.append(start)

    while queue:
        node = queue.pop(0)

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited

def bfs2(graph,startNode):
    visited = list()
    queue= Queue()

    queue.put(startNode)

    while queue.qsize() > 0:
        node = queue.get()

        if node not in visited:
            visited.append(node)
            for i in graph[node]:
                queue.put(i)

    return visited

print(bfs(graph,'E'))
print(bfs2(graph,'E'))


''' 
 < Queue >
  
- FIFO : First In, First Out (선입선출)
- put(), get() 사용 

1. 일반적인 Queue

  data_queue = queue.Queue() 
  data_queue.put(1) # 1 
  data_queue.put(2) # 1 - 2 
  data_queue.put(3) # 1 - 2 - 3 

  data_queue.get() # 1 출력
  data_queue.get() # 2 출력

2. LifoQueue()
: 나중에 입력된 데이터가 먼저 출력되는 구조(Stack과 동일)

  data_queue = queue.LifoQueue() 
  data_queue.put(1) # 1 
  data_queue.put(2) # 2 - 1 
  data_queue.put(3) # 3 - 2 - 1 

  data_queue.get() # 3 출력 
  data_queue.get() # 2 출력

3. PriorityQueue()
: 데이터마다 우선순위를 지정하여, 정렬된 큐로, 우선순위 높은 순으로 출력하는 자료 구조

  data_queue = queue.PriorityQueue()
  data_queue.put((10, 1)) # (10,1)
  data_queue.put((5, 2)) # (5, 2) - (10,1)
  data_queue.put((15, 3)) # (5, 2) - (10, 1) - (15,3)
  
  data_queue.get() # (5,2) 출력
  data_queue.get() # (10, 1) 출력




 < Stack >

- LIFO : Last-In-First-Out (후입선출)
- 스택에서 top을 통해 삽입하는 연산을 'push' , top을 통한 삭제하는 연산을 'pop'이라고 한다.
- push() , pop()   // list의 append, pop 와 같음

1.  장점
- 구조가 단순하고, 구현이 쉽습니다.
- 데이터 저장/불러오는 속도가 빠릅니다.

2.  단점
- 데이터 최대 갯수를 사전에 정해주어야 합니다. (python 재귀 함수는 1000번까지 가능)
- 저장 공간 낭비가 발생할 수 있습니다. (미리 최대 갯수를 넣을 공간을 확보하기 때문)
- 단점이 상당히 크기때문에 보통 배열로 대체하여 사용합니다.



'''

'''
출력

0번째 current : E
0번째 visited : ['E']
0번째 queue : ['D', 'A']

1번째 current : D
1번째 visited : ['E', 'D']
1번째 queue : ['A', 'E', 'F']

2번째 current : A
2번째 visited : ['E', 'D', 'A']
2번째 queue : ['E', 'F', 'E', 'C', 'B']

3번째 current : E
3번째 current : F
3번째 visited : ['E', 'D', 'A', 'F']
3번째 queue : ['E', 'C', 'B', 'D']

4번째 current : E
4번째 current : C
4번째 visited : ['E', 'D', 'A', 'F', 'C']
4번째 queue : ['B', 'D', 'A']

5번째 current : B
5번째 visited : ['E', 'D', 'A', 'F', 'C', 'B']
5번째 queue : ['D', 'A', 'A']

6번째 current : D
6번째 current : A
6번째 current : A

최종 : ['E', 'D', 'A', 'F', 'C', 'B']

'''