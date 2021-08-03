'''
tickets	return
[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	["ICN", "JFK", "HND", "IAD"]
[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
'''

from collections import defaultdict
from collections import deque

def solution(tickets):
    # 키에 따라 값들이 여러개 있을 때 묶기위해 dafaultdict(list) 사용
    routes = defaultdict(list)
    # 중요 : 문제에서 항상 "ICN"공항에서 출발한다고 써있음
    # tickets[0][0]으로 지정하면 -> 1,4번 테케 통과x
    stack = deque(["ICN"])
    answer = deque()

    # 각 출발지에서 가는 경로가 여러개일 경우 묶기
    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])

    # 이때 여러 경로 중 오름차순으로 설정하기 위해 만듬
    for key in routes.keys() :
        routes[key].sort()


    while stack :
        current_land = stack[-1]
        # 더이상 도착지가 존재하지 않을 경우 answer에 마지막 도착지를 pop을 해줍니다.
        # 이때 마지막 도착지에서 출발지를 찾아 answer에 넣어주므로 appendleft를 사용
        if not routes[current_land] :
            answer.appendleft(stack.pop())
        # 갈 수 있는 경로가 아직 존재할 경우, 계속 stack에 쌓아줍니다.
        else :
            stack.append(routes[current_land].pop(0))
    return list(answer)

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
print(solution([["ICN", "BBB"],["ICN", "CCC"],["BBB", "CCC"],["CCC", "BBB"],["CCC", "ICN"]]))