'''
phone_number	return
"01033334444"	"*******4444"
"027778888"	"*****8888"
'''

def solution(phone_number):
    answer = []
    for i in range(len(phone_number)) :
        if i < len(phone_number)-4 :
            answer.append("*")
        else :
            answer.append(phone_number[i])
    return "".join(answer)

print(solution("027778888"))