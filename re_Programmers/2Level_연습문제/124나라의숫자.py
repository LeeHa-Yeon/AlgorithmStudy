'''
n	result
1	1
2	2
3	4
4	11
'''


def solution(n):
    answer = ''
    while n > 0:
        result = divmod(n,3)
        answer = str(result[1]) + answer
        n = result[0]
        if result[1] == 0:
            n = n-1
    return answer.replace('0','4')

print(solution(14))