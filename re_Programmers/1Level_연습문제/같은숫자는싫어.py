'''
arr	answer
[1,1,3,3,0,1,1]	[1,3,0,1]
[4,4,4,3,3]	[4,3]

'''

def solution(arr):
    answer = [arr[0]]
    for p1, p2 in zip(arr.copy(), arr[1:].copy()):

        if p1 == p2 :
            continue
        else :
            answer.append(p2)
    return answer

print(solution([1,1,3,3,0,1,1]))