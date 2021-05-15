'''
N	answer
123	6
987	24
'''

def solution(n):
    n = list(str(n))
    sum = 0
    for i in n :
        sum+=int(i)
    return sum

print(solution(987))