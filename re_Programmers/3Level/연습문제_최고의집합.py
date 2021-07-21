'''
n	s	result
2	9	[4, 5]
2	1	[-1]
2	8	[4, 4]
'''


def solution(n, s):
    if n > s:
        return [-1]

    result = []
    q, r = divmod(s, n)

    for _ in range(n):
        result.append(q)

    for i in range(r):
        result[i] += 1

    result.sort()

    return result

print(solution(2,9))