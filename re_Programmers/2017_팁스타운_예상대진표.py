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
'''