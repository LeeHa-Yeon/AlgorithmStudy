# 문제25 : 원의 넓이를 구하세요
# 반지름의 길이 x 반지름의 길이 x 3.14
# 입력을 반지름의 길이로 정수 n이 주어지면 원의 넓이를 반환하는 함수를 만들어 주세요

def Circle(r) :
    result = r*r*3.14
    return result

n = int(input())

print(Circle(n))