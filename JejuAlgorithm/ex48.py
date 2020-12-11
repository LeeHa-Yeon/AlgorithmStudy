# 문제 : 대소문자 바꿔서 출력하기
# 문자열이 주어지면 대문자와 소문자를 바꿔서 출력하는 프로그램 작성

str1 = 'AAABBBcccddd'
str2 = ''

for i in str1 :
    if i.isupper() :
        str2+=i.lower()
    else :
        str2+=i.upper()

print(str2)