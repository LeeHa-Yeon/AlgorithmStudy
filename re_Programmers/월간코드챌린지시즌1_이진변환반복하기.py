'''
s	result
"110010101001"	[3,8]
"01110"	[3,3]
"1111111"	[4,1]
'''


def solution(s):
    cnt = 0
    resultLen = 0

    while s != "1":
        beforeLen = len(s)
        s = s.replace("0", "")
        afterLen = len(s)
        resultLen += beforeLen - afterLen
        s = bin(afterLen)[2:]
        cnt += 1

    return [cnt, resultLen]

print(solution("110010101001"))