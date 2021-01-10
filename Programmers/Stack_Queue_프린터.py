'''
현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와
내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때,
내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요
priorities	        location	return
[2, 1, 3, 2]	    2       	1
[1, 1, 9, 1, 1, 1]	0       	5
'''

from collections import deque

def solution(priorities, location):
    cnt =0
    result = deque()
    item = [[i,k] for i,k in enumerate(priorities)]

    while len(item) > 0 :
        element = item.pop(0)
        if any(element[1]<maxElement[1] for maxElement in item) :
            item.append(element)
        else :
            result.append(element)

    for i in result :
        cnt+=1
        if i[0] == location :
            return cnt
    return 0



print(solution([1, 1, 9, 1, 1, 1],0))