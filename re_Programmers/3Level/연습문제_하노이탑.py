
'''
n	result
2	[ [1,2], [1,3], [2,3] ]
'''

def solution(n) :
    answer = []
    def hanio(n,start,end,assist) :
        if n == 1 :
            return answer.append([start, end])
        else :
            hanio(n-1,start,assist,end)
            answer.append([start,end])
            hanio(n-1,assist,end,start)
    hanio(n,1,3,2)
    return answer

print(solution(2))