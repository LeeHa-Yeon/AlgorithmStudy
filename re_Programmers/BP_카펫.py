'''
brown	yellow	return
10	    2	    [4, 3]
8	    1	    [3, 3]
24      24  	[8, 6]
'''

import math
def solution(brown, yellow):
    middle = (4-brown)//2
    yellowRow = int((-middle+math.sqrt(pow(middle,2)-(4*yellow)))//2)
    yellowCol = int((-middle-math.sqrt(pow(middle,2)-(4*yellow)))//2)
    return [yellowRow+2,yellowCol+2]

print(solution(10,2))
print(solution(8,1))
print(solution(24,24))