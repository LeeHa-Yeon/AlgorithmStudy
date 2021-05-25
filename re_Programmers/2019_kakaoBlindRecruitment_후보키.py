'''
relation	result
[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]	2
'''

from itertools import combinations
def solution(relations):
    row = len(relations)
    col = len(relations[0])

    idxList = []
    for i in range(1,col+1) :
        idxList.extend(combinations(range(col),i))
    #idxList = sorted(idxList, key=lambda x: x[0])

    final = []
    for keys in idxList:
        tmp = [tuple([item[key] for key in keys]) for item in relations]
        if len(set(tmp)) == row:
            final.append(keys)

    answer = set(final[:])
    for i in range(len(final)):
        for j in range(i + 1, len(final)):
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])

    return len(answer)


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))



