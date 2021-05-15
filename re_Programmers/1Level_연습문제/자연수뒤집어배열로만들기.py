'''
n	return
12345	[5,4,3,2,1]
'''

def solution(n):
    return list(reversed(list(map(int,list(str(n))))))

print(solution(12345))