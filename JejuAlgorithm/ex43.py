# 43번 문제 : 10진수를 2진수
# 사용자에게 숫자를 입력받고 이를 2진수를 바꾸고 그 값을 출력해주세요
# (bin 함수를 사용하지 않고 풀어주세요)

# 입력 : 13
# 출력 : 1101

# 방법 1
print("--------> 방법 1  : 그냥 코드 짜기")
num = 13
binaryList = []

while num !=0 :
    bin1 = num % 2
    binaryList.append(bin1)
    num = num // 2

binaryList.reverse()

print("".join(map(str,binaryList)))


print("--------> 방법 2 : bin(),oct(),hex() 내장함수 사용")
num1 = 13
b = bin(num1)
o = oct(num1)
h = hex(num1)

print("2진수 :",b, end="\n")
print("8진수 :",o, end="\n")
print("16진수 :",h, end="\n")


print("--------> 방법 3 : format() 내장함수 사용")

num2 = 13
b2 = format(num2,'#b')
o2 = format(num2,'#o')
h2 = format(num2,'#x')

print("2진수 :",b2, end="\n")
print("8진수 :",o2, end="\n")
print("16진수 :",h2, end="\n")

print("--------> 방법 4: format() 내장함수 사용2 (#빼고)")

num2 = 13
b2 = format(num2,'b')
o2 = format(num2,'o')
h2 = format(num2,'x')

print("2진수 :",b2, end="\n")
print("8진수 :",o2, end="\n")
print("16진수 :",h2, end="\n")

print("--------> 방법 5: 문자열.format()를 사용한 진수 변환")

num3 = 13
b2 = "{0:#b}".format(num3)
o2 = "{0:#o}".format(num3)
h2 = "{0:#x}".format(num3)
d2 = "{0:#d}".format(num3)

print("2진수 :",b2, end="\n")
print("8진수 :",o2, end="\n")
print("16진수 :",h2, end="\n")
print("10진수 :",d2, end="\n")

print("--------> 방법 6: 문자열.format()를 사용한 진수 변환2(#빼고)")

num3 = 13
b2 = "{0:b}".format(num3)
o2 = "{0:o}".format(num3)
h2 = "{0:x}".format(num3)
d2 = "{0:d}".format(num3)

print("2진수 :",b2, end="\n")
print("8진수 :",o2, end="\n")
print("16진수 :",h2, end="\n")
print("10진수 :",d2, end="\n")











#  "".join(리스트)