# progresses	speeds	return
# [93, 30, 55]	[1, 30, 5]	[2, 1]
# [95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]



from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    completeDays = deque()

    for i in range(len(progresses)) :
        # 테스트케이스11 불통 -> math.ceil 쓸땐 /로 해야 올림이 됨
        completeDays.append(math.ceil((100 - progresses[i]) / speeds[i]))


    while completeDays :
        standard = completeDays.popleft()
        cnt = 1
        for day in completeDays:
            if standard >= day:
                cnt += 1
            else:
                break

        for _ in range(cnt-1):
            completeDays.popleft()

        answer.append(cnt)

    return answer

print(solution([93, 30, 55],[1, 30, 5]))
