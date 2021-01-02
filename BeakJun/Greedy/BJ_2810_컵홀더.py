# *S*LL*LL*S*S*LL*

# 방법 1
n = int(input())
seatType = input()

seatTemp = seatType.replace('LL','T')
seatTemp = "*".join(seatTemp)
seatTemp = "*"+seatTemp+"*"

seatType = seatTemp.replace('T','LL')
cnt = seatType.count('S') + seatType.count('L')

if seatType.count('*') < cnt :
    print(seatType.count('*'))
else :
    print(cnt)



# 컵 홀더 출력 -> 틀린 원인
# n = int(input())
# seatType = list(input())
# i = 0
# while i < len(seatType) :
#     if seatType[i] == 'L' and seatType[i+1] == 'L' :
#         seatType[i] = 'T'  # Temp
#         seatType.pop(i+1)
#     i+=1
# seatType = "*".join(seatType)
# seatType = "*"+seatType+"*"
# cnt = seatType.count('*')
#
# print(cnt)

# 컵 홀더만 출력  -> 틀린 원인
# n = int(input())
# seatType = list(input())
#
# i = 0
# cnt = 0
#
# while i < len(seatType) :
#     if seatType[i] == 'L' and seatType[i+1] == 'L' :
#         seatType[i] = 'S'  # Temp
#         seatType.pop(i+1)
#     i+=1

# seatType = "*".join(seatType)
# seatType = "*"+seatType+"*"
#
# print(seatType.count('*'))

