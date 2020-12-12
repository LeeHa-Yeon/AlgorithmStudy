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




'''
< 정규식 >

j* : *는 j문자가 없거나 0개이상의 j문자를 의미

j\* : 앞에 백슬래시가 있으면 *는 문자로 변환되며, 이것을 이스케이프 됬다고 말합니다. 따라서 j*와 같은 문자를 대응 가능

j\\* : j\* 자체를 패턴으로 만들려면 백슬래시 자체를 이스케이프 시켜줘야됩니다.

즉 위 정규식에서 사용한 \ 문자가 문자열 자체임을 알려 주기 위해 백슬래시 2개를 사용하여 이스케이프 처리를 해야 한다.
'''