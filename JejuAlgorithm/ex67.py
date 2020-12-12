# 문제67 : 민두의 악수
# 참가자인 민두는 몇명의 사람들과 악수를 한 후 중간에 일이 생겨 집으로 갔다.
# 이 행사에서 진행된 악수는 총 n 번이라 했을 때
# 민두는 몇번의 악수를 하고 집을 갔고 이때 민두를 포함한 행사 참가자는 몇명일까?
#
# 악수는 모두 1대 1로 진행이 된다.
# 민두를 제외한 모든 참가자는 자신을 제외한 참가자와 모두 한번씩 악수를 한다.
# 같은 상대와 중복된 악수는 카운트 하지 않는다.
# 민두를 제외한 참가자는 행사를 모두 마쳤다.
# 입력 : 행사에서 진행된 악수 횟수 59
# 출력 : [민두의 악수횟수, 행사참가자][4,12]

n = 59
participant = 0
answer = []

def solution(n,participant) :
    standard = (participant-2)*(participant-1)//2
    if n < standard :
        return participant-1
    participant+=1
    return solution(n,participant)


participant = solution(n,participant)
count = n - (participant-2)*(participant-1)//2
answer.append(count)
answer.append(participant)

print(answer)



'''
1~(k-1) 더한 식 : (k-1)k/2
민수 포함 k명
민수 제외한 모든 참가자가 악수를 한 식 (k-2)(k-1)/2
민수의 악수횟수 count
행사에서 진행된 악수 횟수 n

(k-2)(k-1)/2 + count = n

'''