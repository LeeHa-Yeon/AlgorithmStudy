# 문제 79 : 순회하는 리스트

# 순회전 리스트 = [10,20,25,27,34,35,39]
# n번 순회 후 리스트 = [35,39,10,20,25,27,34]
# 여기서 변하기 전 원소와 변한 후의 원소의 값의 차가 가장 작은 것을 출력하는 프로그램을 작성하세요.
#
# 예를 들어 2번 순회했을 때
# 순회 전 리스트 = [10,20,25,27,34,35,39]
# 순회 후 리스트 = [35,39,10,20,25,27,34]
# 리스트의 차 = [25,19,15,7,9,8,5]
#
# 39와 변한 후의 34 값의 차가 5이므로 리스트의 차 중 최솟값 입니다.
# 따라서 39와 34의 인덱스인 6과 39,34를 출력하는 프로그램을 만들어주세요.

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



