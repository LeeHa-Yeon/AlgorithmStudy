# 문제29 : 대문자만 지나가세요
# 알파벳 하나만을 입력하고 그 알파벳이 대문자이면 YES 아니면 NO를 출력하는 프로그램

alphabet = input()

if ord(alphabet) >= 65 and ord(alphabet) <= 90 :
    print('YES')
else :
    print('No')