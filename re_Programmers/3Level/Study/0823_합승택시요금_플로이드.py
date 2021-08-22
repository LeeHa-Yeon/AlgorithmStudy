def solution(n, s, a, b, fares):
    INF = int(1e9)
    answer = INF
    distance = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        distance[i][i] = 0
    for x, y, cost in fares:
        distance[x][y] = distance[y][x] = cost

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    for i in range(1, n + 1):
        answer = min(answer, distance[s][i] + distance[i][a] + distance[i][b])
    return answer


print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))