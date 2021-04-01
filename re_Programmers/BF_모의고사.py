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


#
# from itertools import chain, repeat
#
# def solution(answers): # 10
#     answer = []
#     collection = []
#     people = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]] # 5
#
#     for i in range(3) :
#         p = people[i]
#         if len(answers) > len(people[i]) :
#             n = divmod(len(answers), len(people[i]))
#             if n[1] == 0:
#                 people[i] = list(chain.from_iterable(repeat(people[i],n[0])))
#             else :
#                 people[i] = list(chain.from_iterable(repeat(people[i],n[0])))+p[:n[1]]
#         else :
#             people[i] = p[:len(answers)]
#
#     for j in range(len(answers)) :
#
#         people[0][j] = 0 if answers[j] == people[0][j] else 9
#         people[1][j] = 0 if answers[j] == people[1][j] else 9
#         people[2][j] = 0 if answers[j] == people[2][j] else 9
#
#     for k in range(3) :
#         collection.append(people[k].count(0))
#
#     for i in range(3):
#         if collection[i] == max(collection):
#             answer.append(i + 1)
#
#
#     return answer