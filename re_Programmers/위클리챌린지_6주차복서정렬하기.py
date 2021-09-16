'''
weights	head2head	result
[50,82,75,120]	["NLWL","WNLL","LWNW","WWLN"]	[3,4,1,2]
[145,92,86]	["NLW","WNL","LWN"]	[2,3,1]
[60,70,60]	["NNN","NNN","NNN"]	[2,1,3]
'''
'''
전체승률이 높은 복서가 앞
동일승률일 경우 무거운복서이긴횟수가 많은 복서가 앞
무거운복서이긴횟수가 동일할 경우 무거운복서가 앞
모두 동일한 경우 -> 복서번호가 작은 번호가 앞
'''

def solution(weights, head2head):
    answer = []
    winOrder = []
    turn = 0

    for head in head2head :
        myInfo = []
        winCnt = head.count("W")
        loseCnt = head.count("L")
        turn += 1

        # 본인차례, 승률 계산하기
        myInfo.append(turn)
        if winCnt+loseCnt != 0 :
            myInfo.append((winCnt / (loseCnt + winCnt)) * 100)
        else :
            myInfo.append(0)

        # 무거운 복서 이긴 횟수
        heavyBoxerWin = 0
        for idx in range(len(weights)):
            if idx == turn-1:
                continue
            if weights[turn-1] < weights[idx] and head[idx] == "W":
                heavyBoxerWin += 1
        myInfo.append(heavyBoxerWin)

        # 본인 무게
        myInfo.append(weights[turn-1])

        # 모든 정보 winOrder에 넣기
        winOrder.append(myInfo)

    # 정렬하기
    winOrder.sort(key=lambda x:(-x[1],-x[2],-x[3],x[0]))

    for boxer in winOrder :
        answer.append(boxer[0])

    return answer


print(solution([50,82,75,120],["NLWL","WNLL","LWNW","WWLN"]))
print(solution([145,92,86],["NLW","WNL","LWN"]))
print(solution([60,70,60],["NNN","NNN","NNN"]))