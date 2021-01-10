'''
citations	                return
[3, 0, 6, 1, 5]	            3
[12, 11, 10, 9, 8, 1]       5
[6, 6, 6, 6, 6, 1]          5
[4, 4, 4]                   3
[4, 4, 4, 5, 0, 1, 2, 3]    4
[10, 11, 12, 13]            4
[3, 0, 6, 1, 5]             3
[0, 0, 1, 1]                1
[0, 1]                      1
[10, 9, 4, 1, 1]            3
'''


def solution(citations):
    cnt = 0
    citations.sort(reverse=True)
    item = [(i+1,k) for i,k in enumerate(citations)]

    # print(item)

    for i in item :
        if i[0] <= i[1] :
            cnt+=1
    return cnt


print(solution([6, 6, 6, 6, 6, 1]))



''' 더 간결하게
def solution(citations):
    cnt = 0
    citations.sort(reverse=True)

    for i in range(len(citations)) :
        if i+1 <= citations[i] :
            cnt+=1
    return cnt
'''