'''
seoul	return
["Jane", "Kim"]	"김서방은 1에 있다"
'''

def solution(seoul):
    idx = str(seoul.index("Kim"))
    return "김서방은 "+idx+"에 있다"

print(solution(["Jane", "Kim"]))