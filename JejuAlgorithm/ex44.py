# 문제 : 각 자리수의 합

# 사용자가 입력한 양의 정수의 각 자리수의 합을 구하는 프로그램을 만들어주세요
# 예를 들어 18234 = 1+8+2+3+4 이고 정답은 18입니다.
# 3849 = 3+8+4+9이고 정답은 24입니다.

print("--------> 방법 1 ")
num = 3849
numList = []

while num > 0 :
    rest = num % 10
    num = num // 10
    numList.append(rest)

print(sum(numList))


print("--------> 방법 2 ")

num1 = 3849
numList2 = []

for i in str(num1) :
    numList2.append(int(i))

print(sum(numList2))


