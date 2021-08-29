'''
user_id	banned_id	result
["frodo", "fradi", "crodo", "abc123", "frodoc"]	["fr*d*", "abc1**"]	2
["frodo", "fradi", "crodo", "abc123", "frodoc"]	["*rodo", "*rodo", "******"]	2
["frodo", "fradi", "crodo", "abc123", "frodoc"]	["fr*d*", "*rodo", "******", "******"]	3
'''

from itertools import permutations
def isMatch(userIdPerm, banIdList):

    for i in range(len(banIdList)) :
        if len(userIdPerm[i]) != len(banIdList[i]) :
            return False
        for j in range(len(userIdPerm[i])) :
            if banIdList[i][j] == "*" :
                continue
            if banIdList[i][j] != userIdPerm[i][j] :
                return False
    return True

def solution(user_id, banned_id):
    answer = []
    for userIdPerm in permutations(user_id,len(banned_id)) :
        if isMatch(userIdPerm,banned_id) :
            findId = list(userIdPerm)
            findId.sort()
            if findId not in answer :
                answer.append(findId)
    return len(answer)




print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))