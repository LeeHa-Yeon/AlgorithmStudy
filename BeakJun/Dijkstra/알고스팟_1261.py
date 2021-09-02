import heapq as hq
import sys

M,N = map(int,sys.stdin.readline().split(" "))
visited = [[0]*M for _ in range(N+1)]
maze = [list(map(int, input().rstrip())) for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

queue = []
hq.heappush(queue,[0,0,0])

while queue :
    weight,cx,cy = hq.heappop(queue)
    if visited[cy][cx] :
        continue
    visited[cy][cx] = 1
    if cx==M-1 and cy==N-1 :
        print(weight)
        break
    for i in range(4) :
        if 0 <= cx + dx[i] < M and 0 <= cy + dy[i] < N and not visited[cy+dy[i]][cx+dx[i]] :
            if maze[cy+dy[i]][cx+dx[i]] == 1 :
                hq.heappush(queue,[weight+1,cx+dx[i],cy+dy[i]])
            else :
                hq.heappush(queue, [weight , cx + dx[i], cy + dy[i]])
