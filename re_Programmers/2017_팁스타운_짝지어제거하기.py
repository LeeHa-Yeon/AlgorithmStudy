'''
s	result
baabaa	1
cdcd	0
'''


def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0 or stack[-1]!=i :
            stack.append(i)
        else :
            stack.pop()
    if stack == [] :
        return 1
    return 0

print(solution("baabaa"))