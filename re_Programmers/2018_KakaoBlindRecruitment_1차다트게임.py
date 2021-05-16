'''
예제	dartResult	answer	설명
1	1S2D*3T	37	11 * 2 + 22 * 2 + 33
2	1D2S#10S	9	12 + 21 * (-1) + 101
3	1D2S0T	3	12 + 21 + 03
4	1S*2T*3S	23	11 * 2 * 2 + 23 * 2 + 31
5	1D#2S*3S	5	12 * (-1) * 2 + 21 * 2 + 31
6	1T2D3D#	-4	13 + 22 + 32 * (-1)
7	1D2S3T*	59	12 + 21 * 2 + 33 * 2
'''

import re
def solution(dartResult):
    splitDart = re.findall("\d+|\D", dartResult)
    splitDart.append("end")
    idx = 0
    answer = []

    while splitDart[idx]!="end" :
        if splitDart[idx] == '#' :
            answer[-1] = answer[-1]*(-1)
        elif splitDart[idx] == '*' :
            if len(answer) > 1 :
                answer[-1] = answer[-1]*(2)
                answer[-2] = answer[-2]*(2)
            else :
                answer[-1] = answer[-1] * (2)
        elif splitDart[idx] == 'S' :
            answer.append(pow(int(splitDart[idx-1]),1))
            del splitDart[idx - 1]
            del splitDart[idx - 1]
            idx -= 2
        elif splitDart[idx] == 'D' :
            answer.append(pow(int(splitDart[idx-1]),2))
            del splitDart[idx-1]
            del splitDart[idx-1]
            idx-=2
        elif splitDart[idx] == 'T' :
            answer.append(pow(int(splitDart[idx-1]),3))
            del splitDart[idx - 1]
            del splitDart[idx - 1]
            idx -= 2
        idx+=1

    return sum(answer)

print(solution("1S2D*3T"))
