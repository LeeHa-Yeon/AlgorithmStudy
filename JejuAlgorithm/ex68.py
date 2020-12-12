# 문제 68 : 버스 시간표
# 학교가 끝난 지원이는 집에 가려고 합니다.
# 학교 앞에 있는 버스 시간표는 너무 복잡해서 버스 도착시간이 몇 분 남았는지 알려주는 프로그램을 만들고 싶습니다.
# 버스시간표와 현재 시간이 주어졌을 때 버스 도착 시간이 얼마나 남았는지 알려주는 프로그램을 만들어주세요.

# - 버스 시간표와 현재 시간이 입력으루 주어집니다.
# - 출력 포맷은 "00시00분"입니다.
# - 만약 1시간 3분이 남았으면 "01시간03분"으로 출력해야 합니다.
# - 버스 시간표에 현재 시간보다 이전인 버스가 있다면 '지나갔습니다.'라고 출력합니다.

# 버스시간표 : ["12:30","13:20","14:13"]
# 현재시간 : "12:40"
# 출력 : ['지나갔습니다.', '0시간 40분', '1시간 33분']

def changeMinute(time) :
    return int(time.split(':')[0])*60 + int(time.split(':')[1])

def printTime(time) :
    timeTuple = divmod(time,60)
    return '{}시간 {}분'.format(timeTuple[0],timeTuple[1])


busSchedule = ["12:30","13:20","14:13"]
currentTime =  "12:40"
answer = []

for subTime in busSchedule :
    differenceTime = changeMinute(subTime) - changeMinute(currentTime)
    if differenceTime < 0 :
        answer.append('지나갔습니다.')
    else :
        answer.append(printTime(abs(differenceTime)))
print(answer)
