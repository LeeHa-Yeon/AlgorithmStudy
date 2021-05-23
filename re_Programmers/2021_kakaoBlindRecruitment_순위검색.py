'''
info	query	result
["java backend junior pizza 150",
"python frontend senior chicken 210",
"python frontend senior chicken 150",
"cpp backend senior pizza 260",
"java backend junior chicken 80",
"python backend senior chicken 50"]

["java and backend and junior and pizza 100",
"python and frontend and senior and chicken 200",
"cpp and - and senior and pizza 250",
"- and backend and senior and - 150",
"- and - and - and chicken 100",
"- and - and - and - 150"]


[1,1,1,1,2,4]
'''

import re
def solution(info, query):
    answer = []
    for i in query :
        splitQuery = re.sub('^\W|-|and|\s+',' ',i).strip()
        splitQuery = " ".join(splitQuery.split())
        ListQuery = splitQuery.split(' ')
        test = info.copy()
        for j in range(len(ListQuery)) :
            for k in test.copy() :
                if ListQuery[j].isdigit() :
                    end = k.split(' ')
                    if int(ListQuery[j]) > int(end[-1]):
                        test.remove(k)
                else :
                    if ListQuery[j] not in k :
                        test.remove(k)
        answer.append(len(test))
    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))


