# 문제 61 : 문자열 압축하기
# 문자열을 입력받고 연속되는 문자열을 압축해서 표현
# 입력 : aaabbbbcddddaa
# 출력 : a3b4c1d4a2

import  re

str1 = 'aaabbbbcddddaa'

print("--------> 방법 1 : 정규표현식 ")

rule = re.findall('(\w)(\\1*)',str1)
str2 =  ''

for ruleTuple in rule :
    str2+= ruleTuple[0] + str(len(ruleTuple[1])+1)

print(str2)




print("--------> 방법 2 ")

changeString = str1[0]
count = 0
result = ''

for i in str1 :
    if changeString == i :
        count+=1
    else :
        result += changeString + str(count)
        changeString = i
        count = 1

result += changeString + str(count)

print(result)




