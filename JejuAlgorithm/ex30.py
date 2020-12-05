# 문제30 : 문자열 속 문자 찾기
# 문자 pineapple에서 apple이라는 문자가 숨겨져 있습니다. 하연이는 이렇듯 문자열 속에 숨어있는 문자를 찾아보려고 합니다
# 입력으로 첫 줄에 문자열이 주어지고 둘째 줄에 찾을 문자가 주어지면 그 문자가 시작하는 index를 반환하는 프로그램을 만들어 주세요


str = 'pineapple is yummy'

word_find = input()

print(str.find(word_find))