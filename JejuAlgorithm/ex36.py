# 문제36 : 구구단 출력하기
# 1~9까지의 숫자 중 하나를 입력하면 그 단의 구구단 결과를 한 줄에 출력하는 프로그램을 작성하세요
#

user_input = int(input())

for i in range(1,10) :
    print(user_input,"*",i,"=",user_input*i)

print("한줄에 결과 출력 : ",end="")
for i in range(1,10) :
    print(user_input*i , end=" ")