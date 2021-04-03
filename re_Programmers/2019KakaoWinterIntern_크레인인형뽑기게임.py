# board	moves	result
# [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	[1,5,3,5,1,2,1,4]	4

# 찾아서 빼고 answer에 넣고
# answer 인접 숫자들은 제거 후 cnt


def solution(board, moves):
    answer = []
    cnt = 0

    for i in moves :
        for j in range(len(board)) :
            target = board[j][i-1]
            if target != 0 :
                answer.append(target)
                board[j][i-1] = 0
                break
        if len(answer) > 1 and answer[-1] == answer[-2] :
            answer.pop(-1)
            answer.pop(-1)
            cnt+=2

    return cnt


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))
