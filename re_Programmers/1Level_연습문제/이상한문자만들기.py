'''
s	return
"try hello world"	"TrY HeLlO WoRlD"
'''

def solution(s):
    result = []
    splitS = s.split(" ")
    while splitS :
        standard = list(splitS.pop(0))
        for i in range(len(standard)) :
            if i%2 == 0 :
                standard[i] = standard[i].upper()
            else :
                standard[i] = standard[i].lower()
        result.append("".join(standard))
    return " ".join(result)

print(solution("try hello world"))