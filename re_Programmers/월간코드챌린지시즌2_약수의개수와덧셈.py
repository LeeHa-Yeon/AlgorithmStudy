'''
left	right	result
13	17	43
24	27	52
'''

def divisor(num) :
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt+=1
    return cnt


def solution(left, right):
    sum = 0
    for i in range(left,right+1) :
        if divisor(i) % 2 == 0 :
            sum+=i
        else :
            sum-=i
    return sum

print(solution(24,27))