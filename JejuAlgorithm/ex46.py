# 문제46 : str 자료형의 응용
# 1부터20까지의(20 포함) 모든 숫자를 일렬로 놓고 모든 자리수의 총 합을 구하시오
# 예를 들어 10부터 15까지의 모든 숫자를 일렬로 놓으면 101112131415이고 각 자리의 숫자를 21입니다.

# def hap(num) :
#     sum = 0
#     for i in num :
#         sum+=int(i)
#     return sum
#
#
# a,b  = map(int,input().split())
# str1 = ''
#
# for i in range(a,b+1) :
#     str1 += str(i)
#
# print(hap(str1))


a = 101112131415
hap = 0

for i in str(a) :
    hap+=int(i)
print(hap)