'''
n	return
12	28
5	6
'''



def solution(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum+=i
    return sum

print(solution(5))