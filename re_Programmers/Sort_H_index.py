def solution(citations):

    citations.sort(reverse=True)
    cnt = 0

    for i in range(len(citations)) :
        if i+1 <= citations[i] :
            cnt+=1
    return cnt

print(solution([3, 0, 6, 1, 5]))

# 6 5 3 1 0