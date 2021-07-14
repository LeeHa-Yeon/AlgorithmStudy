'''
rows columns swipes result
4 3 [[1,1,2,4,3],[3,2,1,2,3],[4,1,1,4,3],[2,2,1,3,3]]   [23,3,21,9]
2 4 [[3,1,2,2,4],[3,1,2,2,4],[4,2,1,2,3],[1,1,1,2,3]]   [12,10,5,20]
2,2 [[3,1,1,1,2],[1,1,2,2,2],[4,2,1,2,2],[2,1,1,2,1]]   [2,4,3,2]
'''

def solution(rows,columns,swipes) :
    arr = [[r*columns+c for c in range(1,columns+1)] for r in range(rows)]
    answer = []
    for i in range(len(swipes)) :
        for d, r1, c1, r2, c2 in [swipes[i]]:
            a = swipes[i]
            if d == 1:
                # 아래
                arr1 = list(arr[r2 - 1][r1:])
                answer.append(sum(arr1))
                for i in range(r2-r1-1,-1,-1) :
                    tmp = arr[r1+i-1][r1:]
                    arr[r1 + i][r1:] = tmp
                arr[r1-1][r1:] = arr1
            elif d == 2:
                # 위
                arr1 = list(arr[r1-1][:r2])
                answer.append(sum(arr1))
                for i in range(1,r2-r1+1):
                    tmp = arr[r1-1+i][:r2]
                    arr[r1-2+i][:r2] = tmp
                arr[r1][:r2] = arr1
            elif d == 3:
                # 오른쪽
                print(arr[])
                # arr1 = list(list(zip(*arr))[c2-1][r1-1:r2])
                # answer.append(sum(arr1))
                # for i in range(c2-c1-1,-1,-1):
                #     tmp = list(list(zip(*arr))[c2+i-1][r1-1:r2])
                #     arr[r1-2+i][:r2] = tmp
                # arr[r1][:r2] = arr1
            elif d == 4:
                print("왼쪽")
                print(list(zip(*arr))[c1-1][r1-1:r2])

    return arr

print(solution(4,3,[[1,1,2,4,3],[3,2,1,2,3],[4,1,1,4,3],[2,2,1,3,3]]))