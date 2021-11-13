import sys

basicSensorCnt, newSensorCnt = map(int,input().split(" "))

basicSensor = "".join(list(sys.stdin.readline(basicSensorCnt*2).strip().split()))
newSensor = "".join(list(sys.stdin.readline(newSensorCnt*2).strip().split()))

answer = 0

standard = basicSensor[0]
cnt = 1
result = ""
for sensor in basicSensor[1:] :
    if standard == sensor :
        cnt+=1
    else :
        result+=str(cnt)
        cnt=1
        standard = sensor
result+=str(cnt)

print(result)

#
# while result != newSensor :
#     answer += 1