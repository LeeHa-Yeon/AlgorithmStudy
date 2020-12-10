# 문제41 : 소수판별
# 숫자가 주어지면 소수인지 아닌지 판별하는 프로그램 작성
# 소수이면 YES, 소수가 아니면 NO로 출력
# (소수 : 1과 자기 자신만으로 나누어떨어지는 1보다 큰 양의 정수)

def prime(num) :
    if num != 1 :
        for i in range(2,num) :
            if num % i == 0 :
                return False
            else :
                return True
    else :
        return True

sosu = int(input())

if prime(sosu) :
    print("소수 입니다.")
else :
    print("소수가 아닙니다.")



def solution(n):
    num= set(range(2, n+1))
    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
            return num

print(solution(10))



