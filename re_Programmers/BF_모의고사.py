# answers	return
# [1,2,3,4,5]	[1]
# [1,3,2,4,2]	[1,2,3]

from itertools import chain, repeat

def solution(answer) :
    result = [0,0,0]
    student = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    compareArr = []
    Dap = []

    for i in student:
        compareArr.append(list(chain.from_iterable(repeat(i,len(answer)//len(i)+1))))

    for j in range(len(compareArr)) :
        for i in range(len(answer)) :
            if answer[i] == compareArr[j][i] :
                result[j]+=1

    for i in range(3):
        if result[i] == max(result):
            Dap.append(i + 1)


    return Dap




print(solution([1,2,3,4,5])) # 10
