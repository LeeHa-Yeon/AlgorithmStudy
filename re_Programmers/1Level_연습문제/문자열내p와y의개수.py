'''
s	answer
"pPoooyY"	true
"Pyy"	false
'''



def solution(s):
    if s.lower().count('p') == s.lower().count('y') :
        return True
    return False


print(solution("pPoooyY"))