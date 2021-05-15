'''
s	n	result
"AB"	1	"BC"
"z"	1	"a"
"a B z"	4	"e F d"
'''

def solution(s, n):
    answer = []
    for i in s :
        if i == " " :
            answer.append(" ")
            continue
        if i.isupper() :
            if ord(i)+n > 90 :
                answer.append(chr(ord(i)+n-26))
            else :
                answer.append(chr(ord(i)+n))
        else :
            if ord(i)+n > 122 :
                answer.append(chr(ord(i)+n-26))
            else :
                answer.append(chr(ord(i)+n))
    return "".join(answer)

print(solution("a B z",4))
print("----")
print(solution("z",1))