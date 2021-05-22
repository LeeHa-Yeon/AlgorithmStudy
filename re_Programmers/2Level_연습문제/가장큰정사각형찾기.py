'''
board	answer
[[0,1,1,1],
[1,1,1,1],
[1,1,1,1],
[0,0,1,0]]	9

[[0,0,1,1],
[1,1,1,1]]	4
'''

import numpy as np
def solution(board):

    # i는 행, j는 열
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j] == 1:
                # (i,j)위치의 값을 기준으로 왼쪽, 위, 왼쪽 위 대각선 중 가장 작은 값에서 1더해 i,j에 갱신
                board[i][j] = min(board[i][j-1],board[i-1][j],board[i-1][j-1]) + 1

    board = np.array(board)

    return int(board.max()) **2

# print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,0,1,1],[1,1,1,1]]))
