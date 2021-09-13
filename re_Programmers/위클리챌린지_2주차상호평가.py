'''
scores	result
[[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]	"FBABD"
[[50,90],[50,87]]	"DA"
[[70,49,90],[68,50,38],[73,31,100]]	"CFD"
'''

def average(scoreList) :
    scoreSum = sum(scoreList)
    result = scoreSum // len(scoreList)

    if result >= 90 :
        return "A"
    elif result >= 80 and result < 90 :
        return "B"
    elif result >= 70 and result < 80 :
        return "C"
    elif result >= 50 and result < 70 :
        return "D"
    else :
        return "F"

def solution(scores):
    answer = []
    reScores = [[] for i in range(len(scores))]

    for i in range(len(scores)) :
        for j in range(len(scores)) :
            reScores[i].append(scores[j][i])

    for i in range(len(reScores)) :
        maxScore = max(reScores[i])
        minScore = min(reScores[i])
        for j in range(len(reScores)) :
            if i == j :
                if reScores[i].count(reScores[i][j]) > 1 :
                    continue
                elif reScores[i][j] == maxScore or reScores[i][j] == minScore :
                    del reScores[i][j]
        answer.append(average(reScores[i]))

    return "".join(answer)


print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))
print(solution([[50,90],[50,87]]))
print(solution([[70,49,90],[68,50,38],[73,31,100]]))