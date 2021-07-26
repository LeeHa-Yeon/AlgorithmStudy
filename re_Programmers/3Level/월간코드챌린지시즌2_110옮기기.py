'''
s	result
["1110","100111100","0111111010"]	["1101","100110110","0110110111"]
'''

def solution(s):
    answer = []
    for i in s :
        print(i.replace('110',' '))
    return answer

print(solution(["1110","100111100","0111111010"]))