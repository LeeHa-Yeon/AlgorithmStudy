'''
n	result
10	4
5	3
'''

def solution(n):
    num = set(range(2,n+1))
    for i in range(2,n+1):
        if i in num:
            num -= set(range(i*2,n+1,i))
    return num


print(solution(10))