'''
1. 각 블록을 놓을때, 놓을 블록이 차지하는 공간 중 어느 한곳이라도 블록이 놓여있을 경우 빈배열을 return - ok
2. 블록놓을때 블록이 보드 밖으로 나가게 된다면 빈 배열 return - ok
3. 입력 배열에 있는 모든 블록 넣은 뒤 같은 세로열에 있는 숫자 합이 정확히 10인지 확인하고 -> 해당 열의 값 지우기
4. 빈칸은 공백문자로 나머지는 숫자값을 문자로
'''

import numpy as np
def solution(param0):
    arr = [[" " for _ in range(6)] for _ in range(6)]
    divParam0 = [(param0[i],param0[i+1],param0[i+2]) for i in range(0,len(param0),3)]

    while divParam0 :
        p = divParam0.pop(0)
        for i in range(p[2]) :
            if p[0]+i > 5 :
                return []
            if arr[p[1]][p[0]+i] != " " :
                return []
            arr[p[1]][p[0]+i] = i+1

    npArr = np.array(arr)

    for i in range(len(arr)) :
        arrCol = " ".join(colum(npArr,i))
        arrCol = " ".join(arrCol.split())
        result = sum(map(int,arrCol.split(' ')))
        if result == 10 :
            npArr[:,i]=[' ',' ',' ',' ',' ',' ']
    arr = npArr.tolist()

    for i in range(len(arr)) :
        arr[i] = "".join(arr[i])

    return arr

def colum(matrix,i) :
    return [row[i] for row in matrix]