'''
A	B	answer
[1, 4, 2]	[5, 4, 4]	29
[1,2]	[3,4]	10
'''

def solution(A,B):
    answer = []
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)) :
        answer.append(A[i]*B[i])
    return sum(answer)

print(solution([1, 4, 2],[5, 4, 4]))