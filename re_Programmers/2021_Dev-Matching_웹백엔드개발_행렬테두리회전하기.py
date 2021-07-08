'''
rows	columns	queries	result
6	6	[[2,2,5,4],[3,3,6,6],[5,1,6,3]]	[8, 10, 25]
3	3	[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]	[1, 1, 5, 3]
100	97	[[1,1,100,97]]	[1]
'''


def solution(rows, columns, queries):
    arr = [[r*columns+c for c in range(1,columns+1)] for r in range(rows)]
    answer = []

    # 좌표 이동
    for r1,c1,r2,c2 in queries :
        arr1 = []
        temp = arr[r1-1][c1-1]
        arr1.append(temp)

        # 왼쪽
        for i in range(r1-1,r2-1) :
            tempArr = arr[i+1][c1-1]
            arr[i][c1-1] = tempArr
            arr1.append(tempArr)

        # 위
        for i in range(c1-1,c2-1) :
            tempArr = arr[r2-1][i+1]
            arr[r2-1][i] = tempArr
            arr1.append(tempArr)

        # 오른쪽
        for i in range(r2-1,r1-1,-1) :
            tempArr = arr[i-1][c2-1]
            arr[i][c2-1] = tempArr
            arr1.append(tempArr)

        # 아래
        for i in range(c2-1,c1-1,-1) :
            tempArr = arr[r1-1][i-1]
            arr[r1-1][i] = tempArr
            arr1.append(tempArr)
        arr[r1-1][c1] = temp
        answer.append(min(arr1))

    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100,97,[[1,1,100,97]]))