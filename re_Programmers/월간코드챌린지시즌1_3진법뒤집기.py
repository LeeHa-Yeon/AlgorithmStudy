'''
n	result
45	7
125	229
'''

def solution(n):
    answer = ""

    while n>=1 :
        result = divmod(n,3)
        n = result[0]
        answer+=str(result[1])

    return int(answer,3)

print(solution(45))
