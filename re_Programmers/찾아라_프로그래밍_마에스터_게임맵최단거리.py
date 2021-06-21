'''
maps	answer
[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	11
[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]	-1
'''
from collections import deque
def solution(maps):
    row,col = len(maps),len(maps[0])
    dx,dy = [-1,0,1,0],[0,1,0,-1]
    dis = [[1]*col for _ in range(row)]
    Q = deque()
    Q.append((0,0))
    maps[0][0] = 0
    while Q :
        k = Q.popleft()
        for i in range(4) :
            # 왼쪽,위,오른쪽,아
            x = k[0]+dx[i]
            y = k[1]+dy[i]

            if 0<=x<row and 0<=y<col and maps[x][y] == 1 :
                maps[x][y] = 0
                dis[x][y] = (dis[k[0]][k[1]])+1
                Q.append((x,y))

    if dis[row-1][col-1] == 1 :
        return -1
    else :
        return dis[-1][-1]


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))