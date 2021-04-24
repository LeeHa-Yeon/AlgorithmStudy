'''
scores	result
[[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]	"FBABD"
[[50,90],[50,87]]	"DA"
[[70,49,90],[68,50,38],[73,31,100]]	"CFD"

'''


def solution(scores) :
    answer =''

    for i in range(len(scores)) :
        noList = []
        for j in scores :
            noList.append(j[i])
        m = max(noList)
        n = min(noList)
        m_cnt = noList.count(m)
        n_cnt = noList.count(n)

        if m == scores[i][i] and m_cnt < 2 :
            idx = noList.index(m)
            noList.pop(idx)

        if n == scores[i][i] and n_cnt < 2 :
            idx = noList.index(n)
            noList.pop(idx)

        sum = 0
        for i in noList:
            sum += i
        point = sum/len(noList)

        if point >= 90:
            answer += 'A'
        elif point >= 80:
            answer += 'B'
        elif point >= 70:
            answer += 'C'
        elif point >= 50:
            answer += 'D'
        else:
            answer += 'F'
    return answer


print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))
print(solution([[50,90],[50,87]]))
print(solution([[70,49,90],[68,50,38],[73,31,100]]))