
'''
W	H	result
8	12	80

=> 최대 공약수 문제

가로,세로 두 비의 최대 공약수가 반복되고 최대 공약수만큼 꼭지점에서 만난다.

1. 최대 공약수가 1일 경우
-> 직선이 지나는 점이 존재하지 않는다.
-> 대각선이 지나갈때마다 가로개수w,세로개수h만큼 사각형이 갈라진다.
-> w+h-1 ( 1을 빼는 이유는 처음 시작할때 겹치는 사각형 )

2. 최대 공약수g 가 그 이상인 경우
-> w+h-g


=> 즉, (X+Y- 두수의 최대공약수)

'''

import math
def solution(w,h):
    gcf = math.gcd(w,h)
    if gcf == 1 :
        return w*h-(w+h-1)
    return w*h-(w+h-gcf)

print(solution(8,12))

