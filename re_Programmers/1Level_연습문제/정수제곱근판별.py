'''
n	return
121	144
3	-1
'''

import math
def solution(n):
    if int(math.pow(int(math.sqrt(n)),2)) == n:
        return pow(math.sqrt(n)+1,2)
    return -1

print(solution(121))
