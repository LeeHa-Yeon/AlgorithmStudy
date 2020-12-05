# 문제20 : 몫과 나머지
# 공백으로 구분하여 두 숫자가 주어집니다.
# 첫번째 숫자로 두번째 숫자를 나누었을 때 그 몫과 나머지를 공백으로 구분하여 출력하세요

a, b = map(int,input().split(' '))

share = a // b
rest = a % b

print(share, rest, sep= ' ')