# 문제 79 : 순회하는 리스트

def solution(list,n) :
    circuitList = list[:]
    circuit = n % len(circuitList)  # 순회 횟수
    for _ in range(circuit) :
        circuitList.insert(0,circuitList[-1])
        circuitList.pop(-1)
    distanceList = distance(list, circuitList)
    answerIdx = distanceList.index(min(distanceList))
    answerFirst = list[answerIdx]
    answerSecond = circuitList[answerIdx]
    return print(f'인덱스 : {answerIdx}\n순회전 리스트의 값 : {answerFirst}\n순회후 리스트의 값 : {answerSecond}')

def distance(beforeList,afterList) :
    distanceList = []

    for i in range(len(afterList)) :
        distanceList.append(abs(beforeList[i]-afterList[i]))

    return distanceList



solution([10,20,25,27,34,35,39],2)










# def circuitList(list,n) :
#     # 리스트 얕은 복사
#     l = list[:]
#     for i in range(n) :
#         l.insert(0,l[-1])
#         del l[-1]
#     return l
#
# def distance(a,b) :
#     disList = []
#     for i in range(len(a)) :
#         disList.append(abs(a[i]-b[i]))
#     return disList
#
# n = 2
# lBefore = [10,20,25,27,34,35,39]
# lAfter = circuitList(lBefore,n)
# lminus = distance(lBefore,lAfter)
#
# idx = lminus.index(min(lminus))

# print("인덱스 : ",idx)
# print("값 : " , lBefore[idx],lAfter[idx])



