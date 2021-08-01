'''
n	computers	return
3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1
'''



def dfs(n,computers,visited,v) :
    if visited[v] == False:
        visited[v] = True
    for e in range(n) :
        if computers[v][e] == 1 and visited[e] == False :
            dfs(n,computers,visited,e)

def solution(n, computers):
    visited = [False]*n
    cnt = 0
    while False in visited :
        for v in range(n) :
            if visited[v] == False:
                print(visited)
                dfs(n,computers,visited,v)
                cnt += 1
    return cnt

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))