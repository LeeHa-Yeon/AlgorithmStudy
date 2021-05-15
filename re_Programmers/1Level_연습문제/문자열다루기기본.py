'''
s	return
"a234"	false
"1234"	true
'''

def solution(s):
    return s.isdigit() and len(s)==4 or len(s)==6

print(solution("a234"))