# 플로이드와샬 문제
from collections import defaultdict
def solution(n, results):
    win = defaultdict(set)
    lose = defaultdict(set)
    cnt = 0

    for result in results :
        win[result[0]].add(result[1])
        lose[result[1]].add(result[0])

    for i in range(1,n+1) :
        # 힘의 우열로 인해 i를 이긴 사람들은 i가 이긴 사람들 또한 이김
        for winner in lose[i] :
            win[winner].update(win[i])
        # 힘의 우열로 인해 i가 이긴 사람들에게 모두 짐
        for loser in win[i] :
            lose[loser].update(lose[i])
    for i in range(1, n + 1):
        if len(win[i] | lose[i]) == n - 1:
            cnt += 1
    return cnt

print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
# print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])) # 2
# print(solution(7, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [5,6], [6,7]])) # 4
# print(solution(6, [[1,2], [2,3], [3,4], [4,5], [5,6]])) # 6
# print(solution(5, [[1, 4], [4, 2], [2, 5], [5, 3]])) # 5
# print(solution(5, [[3, 5], [4, 2], [4, 5], [5, 1], [5, 2]])) # 1
# print(solution(3, [[1,2],[1,3]]))  # 1
# print(solution(6, [[1,6],[2,6],[3,6],[4,6]])) # 0
# print(solution(8, [[1,2],[3,4],[5,6],[7,8]])) # 0
# print(solution(9, [[1,2],[1,3],[1,4],[1,5],[6,1],[7,1],[8,1],[9,1]])) # 1
# print(solution(6, [[1,2],[2,3],[3,4],[4,5],[5,6],[2,4],[2,6]])) # 6
# print(solution(4, [[4,3],[4,2],[3,2],[3,1],[4,1], [2,1]])) # 4
# print(solution(3,[[3,2],[3,1]])) # 1
# print(solution(4, [[1,2],[1,3],[3,4]])) # 1


# 처음 문제 풀때
'''
from collections import defaultdict
def solution(n, results):
    player = defaultdict(list)

    for result in results :
        player[result[0]].append(result[1])
        player[result[1]].append(result[0])

    for i in range(1,n+1) :
        if len(player[i]) == n-1 :
            print(i)

    return player
'''