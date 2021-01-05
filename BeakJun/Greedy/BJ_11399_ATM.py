# n = int(input())
# pList = list(map(int,input().split(' ')))  # 3 1 4 3 2  ->   2 5 1 4 3
# wList = pList[:]
# a = sorted(pList) # 1 2 3 3 4
# answerList = []
# answer = 0
# result = 0
#
# for i in range(n) :
#     minIdx = pList.index(a[i])
#     pList[minIdx] = 0
#     answerList.append(minIdx+1)
#
# for j in range(n) :
#     idx = answerList[j]
#     b = wList[idx-1]
#     answer+=b
#     result+=answer
#
# print(result)

def solution(n,pList):
    answer = 0
    for i in range(n):
        for j in range(0, i + 1):
            answer += pList[j]
    return answer


n = int(input())
pList = list(map(int, input().split(' ')))
pList.sort()
print(solution(n,pList))