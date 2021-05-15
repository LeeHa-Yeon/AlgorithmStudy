'''
n	return
3	"수박수"
4	"수박수박"
'''

def solution(n):
    answer = '수박'*n
    return answer[:n]

print(solution(4))