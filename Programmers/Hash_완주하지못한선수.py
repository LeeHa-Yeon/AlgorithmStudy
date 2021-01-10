'''
participant	                                completion	                        return
[leo, kiki, eden]	                        [eden, kiki]	                    leo
['leo', 'kiki', 'eden'],['eden', 'kiki']

[marina, josipa, nikola, vinko, filipa]	    [josipa, filipa, marina, nikola]	vinko
['marina', 'josipa', 'nikola', 'vinko', 'filipa'], ['josipa', 'filipa', 'marina', 'nikola']


[mislav, stanko, mislav, ana]	            [stanko, ana, mislav]	            mislav
['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']

'''


def solution(participant, completion):
    test = set(participant)-set(completion)
    participant.sort()
    completion.sort()

    n = len(participant)

    for i in range(n-1) :
        if participant[i] != completion[i] :
            return participant[i]


    return participant[n-1]


print(solution(['leo', 'kiki', 'eden'],['eden', 'kiki']))


''' 정확도, 효율성 일부분 틀림 -> 이유는 정말 모르겠음..

from collections import Counter

def solution(participant, completion):
    answer = ''
    test = set(participant)-set(completion)

    if len(test) == 0 :
        answer = Counter(participant)
        for i,k in answer.items() :
            if k == 2:
                return i

    return test.pop()
    
    
    
------------------------------------ 
    
    
def solution(participant, completion):
    test = set(participant)-set(completion)
    participant.sort()

    if len(test) == 0 :
        for i in range(len(participant)) :
            if participant[i] == participant[i-1] :
                return participant[i]


    return test.pop()
'''