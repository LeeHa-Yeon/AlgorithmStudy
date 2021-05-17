'''
land	answer
[[1,2,3,5],[5,6,7,8],[4,3,2,1]]	16
'''

def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]

    return max(land[-1])

print(solution([[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]))



# 같은값일때 문제점이 발생..
# def solution(land):
#     answer = []
#     current_idx = land[0].index(min(land[0]))
#     for i in land :
#         print(i)
#         # 이전 열에 있으면 안되고
#         # 내가 같은 값이 있다면 다음 열의 큰 수 자리를 피해서
#         if current_idx == i.index(max(i)):
#             print(current_idx, i.index(max(i)))
#             i[i.index(max(i))] = i[land[0].index(min(land[0]))]
#             current_idx = i.index(max(i))
#             answer.append(i[current_idx])
#         else:
#             current_idx = i.index(max(i))
#             answer.append(i[current_idx])
#
#
#
#     return answer
#
#
# print(solution([[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]))
# print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
