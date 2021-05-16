'''
n	m	return
3	12	[3, 12]
2	5	[1, 10]
'''


from math import gcd

def lcm(uc,x,y) :
    return x*y//uc

def solution(n, m):
    uc = gcd(n,m)
    return [uc,lcm(uc,n,m)]

print(solution(3,12))
print(solution(2,5))