'''
word	result
"AAAAE"	6
"AAAE"	10
"I"	1563
"EIO"	1189
'''

# 다른 사람 코드 참고
def solution(words):
    answer = 0
    vowels = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4 }
    arr = [781,156,31,6,1]
    for idx,word in enumerate(words) :
        answer+=((vowels[word]*arr[idx])+1)
    return answer

print(solution("AAAAE"))
print(solution("EIO"))