# 문제 75 : 이상한 369
# 369 게임을 하는데 조금 이상한 규칙이 있습니다.
# 3,6,9일때만 박수를 쳐야합니다.
# 예를 들어 13,16과 같이 3과,6,9만으로 된 숫자가 아닐 경우엔 박수를 치지 않습니다.
# 수현이는 박수를 몇 번 쳤는지 확인하고 싶습니다.
# 36일때 박수를 쳤다면 박수를 친 횟수는 5번입니다.
# n을 입력하면 박수를 몇 번 쳤는지 그 숫자를 출력해주세요.
# 순서
# 1 : 3
# 2 : 6
# 3 : 9
# 4 : 33
# 5 : 36
# 6 : 39
# 7 : 63
# 8 : 66
# 9 : 69
# 10 : 93

'''
함수
1. 3,6,9 를 중복해서 순서대로 정렬 -> 중복순열
2. 한 튜플을 합쳐서 받은 숫자와 비교
3. 받은 숫자가 몇번째인지를 파악
'''
from itertools import product

def solution(num) :
    gameList = []
    count = 0
    for i in range(1,len(str(num))+1) :
        gameList+= list(product([3, 6, 9], repeat=i))

    print(gameList)
    for gameTuple in gameList :
        count+=1
        gameStr = ''
        for gameIndex in gameTuple :
            gameStr+=str(gameIndex)
        if int(gameStr) == num :
            return count
    return count



print(solution(36),"번 박수를 쳤습니다.")
