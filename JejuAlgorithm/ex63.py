# 문제63 : 친해지고 싶어
# 어떤 입력값이 주어지면 앞 글자만 줄여서 출력
# 입력 : 복잡한 세상 편하게 살자
# 출력 : 복세편살

str1 = '복잡한 세상 편하게 살자'
strList = list(map(str,str1.split(' ')))

for i in strList :
    print(i[0],end='')