'''
s	return
"3people unFollowed me"	"3people Unfollowed Me"
"for the last week"	"For The Last Week"
'''

def solution(s):
    s = s.split(" ")
    for i in range(len(s)) :
        if s[i] == '':
            continue
        else :
            print(s[i][0])
            first = s[i][0].upper() if s[i][0].islower() else s[i][0]
            rest = s[i][1:].lower()
            s[i] = first+rest

    return " ".join(s)

print(solution("3people     unFo3llowed me"))