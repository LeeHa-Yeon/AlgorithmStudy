'''
lines   return
["2016-09-15 00:00:00.000 3s"]   1
["2016-09-15 23:59:59.999 0.001s"]  1
["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]    1
["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]    2
["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]   7
["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"]    1
'''
from datetime import datetime,timedelta
def solution(lines):
    rangeList = []
    maxCnt = 0

    for line in lines:
        S = line[:23]
        T = line.split(" ")[2]
        endTime = datetime.strptime(S,'%Y-%m-%d %H:%M:%S.%f')
        startTime = endTime-timedelta(seconds=float(T[:len(T)-1]))+timedelta(milliseconds=1)
        rangeList.append((startTime,endTime))

    def cnt_secRange(standard):
        cnt = 0
        startStandard = standard + timedelta(milliseconds=1000)
        endStandard = standard
        for s,e in rangeList:
            if s < startStandard and e >= endStandard :
                cnt += 1
        return cnt

    for s,e in rangeList :
        maxCnt = max(maxCnt,cnt_secRange(s),cnt_secRange(e))

    return maxCnt


print(solution(["2016-09-15 00:00:00.000 3s"]))
print(solution(["2016-09-15 23:59:59.999 0.001s"]))
print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
print(solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]))
print(solution(["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"]))