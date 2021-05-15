'''
a	b	return
3	5	12
3	3	3
5	3	12
'''

def solution(a, b):
    if a > b :
        a,b = b,a
    return sum(range(a,b+1))