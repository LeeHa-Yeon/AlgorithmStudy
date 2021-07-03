'''
n	result
4	[1,2,9,3,10,8,4,5,6,7]
5	[1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
6	[1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]

풀이방식
1) 피라미드 -> 직각삼각형모양
2) 좌표로 생각하기
3) 마지막 2차원 리스트 -> 1차원 합칠때 itertools chain 사용
'''


from itertools import chain
def solution(n):
    # 삼각형 배열 만들기
    answer = [[0 for _ in range(0,i)] for i in range(1,n+1)]

    # 좌표 초기화, 처음 시작 숫자
    x,y = -1,0
    num = 1

    # 좌표 이동에 따라 해당 좌표에 값 넣어주기 ( 아래,옆,위 3가지밖에 없으므로 3으로 나누기 )
    for i in range(n) :
        for _ in range(n-i) :
            # 만약 나머지가 0일 경우 x좌표만 +1됨 ( 아래 )
            if i%3 == 0 :
                x+=1
            # 만약 나머지가 1일 경우 y좌표만 +1됨 ( 옆 )
            elif i%3 == 1 :
                y+=1
            # 만약 나머지가 2일 경우 둘다 -1됨 ( 위 )
            else :
                x-=1
                y-=1
            answer[x][y] = num
            num+=1

    return list(chain.from_iterable(answer))

print(solution(4))