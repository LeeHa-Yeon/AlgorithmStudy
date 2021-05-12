'''
N	stages	result
5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
4	[4,4,4,4,4]	[4,1,2,3]
'''

def solution(N, stages):
    answer = []
    stages.sort()

    for i in range(1,N+1):
        stage =stages.count(i)
        if len(stages) > 0 :
            answer.append(stage/len(stages))
        else :
            answer.append(0)
            continue
        while stage :
            stages.pop(0)
            stage-=1

    result = []
    for _ in range(len(answer)) :
        idx = answer.index(max(answer))
        answer[idx] = -1
        result.append(idx+1)
    return result

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,[4,4,4,4,4]))
