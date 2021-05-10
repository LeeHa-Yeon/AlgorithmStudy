'''
N	A	B	answer
8	4	7	3
'''


def solution(n, a, b):
    answer = 0
    while a != b:
        answer += 1
        a = (a + 1) // 2
        b = (b + 1) // 2
    return answer

print(solution(8,4,5))


'''
def solution(n,a,b):
    l = [ i+1 for i in range(n)]
    participant = []
    round = 1

    # 초기 참여자 대진표 만들기
    # [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16]]
    for i in range(0, len(l), 2):
        participant.append(l[i:i+2])

        if [a,b] in participant :
            return round

    win = []
    winresult =[]
    cnt = 0

    while [a,b] not in participant and participant :
        p = participant.pop(0)

        if a in p :
            win.append(a)
        elif b in p:
            win.append(b)
        else:
            win.append(p[0])
        cnt += 1
        if cnt % 2 == 0:
            winresult.append(win)
            win = []

        if len(participant) == 0 :
            participant = winresult[:]
            winresult = []
            win = []
            round+=1


    return round
'''