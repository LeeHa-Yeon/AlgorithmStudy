'''
progresses              	speeds	            return
[93, 30, 55]	            [1, 30, 5]	        [2, 1]
[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]
'''

from collections import deque

def solution(progresses, speeds):
    totalDay,result = [],[]
    dp = deque(progresses)

    # 각 progresses별로 결린 경과시간 구하기
    for i in range(len(progresses)) :
        progresse = dp.popleft()
        day = 0
        while progresse < 100 :
            progresse+=speeds[i]
            day+=1
        totalDay.append(day)

    # totalDay 기준날로부터 기준날보다 적은 날을 합산
    totalDay = deque(totalDay)
    while totalDay :
        standard = totalDay.popleft()
        cnt = 1
        for day in totalDay :
            if standard >= day :
                cnt += 1
            else :
                break

        for _ in range(cnt-1) :
            totalDay.popleft()

        result.append(cnt)

    return result


print(solution([93, 30, 55]	,[1, 30, 5]))