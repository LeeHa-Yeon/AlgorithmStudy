def solution(m, n, puddles):
    answer = [[0 for _ in range(m)] for _ in range(n)]
    answer[0][0] = 1

    for x in range(n):
        for y in range(m):
            if x==y==0 :
                continue
            if [y+1,x+1] in puddles:
                answer[x][y] = 0
            else:
                if x == 0:
                    answer[x][y]+=answer[x][y - 1]
                elif y == 0:
                    answer[x][y]+=answer[x - 1][y]
                else:
                    answer[x][y]+=(answer[x - 1][y] + answer[x][y - 1])
    return answer[-1][-1]%1000000007

print(solution(4,3,[[2, 2]]))