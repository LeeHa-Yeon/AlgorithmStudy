# 문제35 : Factory함수 사용하기
# 2제곱, 3제곱, 4제곱을 할 수 있는 Factory함수를 만들려고 합니다.
# $에 코드를 작성하여 two함수를 완성하세요

def Squared(n):
    def num(value):
        return value ** n
    return num

a = Squared(2)
b = Squared(3)
c = Squared(4)

print(a(10))
print(b(10))
print(c(10))