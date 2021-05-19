'''
s	answer
"()()"	true
"(())()"	true
")()("	false
"(()("	false
'''


def solution(s):
    if s.count('(')!=s.count(')') :
        return False
    s = s.replace('()','')
    if s == '' :
        return True
    if s[0] == ')' or s[-1] == '(' :
        return False
    return True


print(solution("()()"))