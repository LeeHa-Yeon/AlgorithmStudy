'''
N	A	B	answer
8	4	7	3
'''


def solution(n, a, b):
    next_round = 0

    while a != b:
        a = (a+1) // 2
        b = (b+1) // 2
        next_round += 1

    return next_round

print(solution(8,2,3))
