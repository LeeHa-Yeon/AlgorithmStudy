'''
스터디 그룹 -> 대표자 선정
n       t1                  t2                  answer
10      [9,4,4,4,7]         [2,10,7,6,3]        [1,2,5,6,8]
10      [6,3,4,9,2,7,5]     [4,2,8,2,1,10,3]    [3,6,7]
'''

import heapq

def solution(n,t1,t2):
    newGroup = []

    # solo 대표자
    solo = set()
    for i in range(1,n+1) :
        solo.add(i)
    result = sorted(solo - set(t1) - set(t2))


    # group 대표자
    for i in range(len(t1)) :
        newGroup.append(sorted([t1[i],t2[i]]))
    print(sorted(newGroup))

    # while newGroup :
    #     print(newGroup)
    #     a = newGroup.pop(0)
    #     delIndx= []
    #     for k,i in enumerate(newGroup) :
    #         if a & i :
    #             a = a.union(i)
    #             delIndx.append(i)
    #             print(a)
    #         else :
    #
    #             s = sorted(a)
    #             idx = len(a) // 2
    #             print("s", s)
    #             if len(a) % 2 == 0 :
    #                 result.append(s[idx-1])
    #             else :
    #                 result.append(s[idx])
    #     while delIndx :
    #         newGroup.remove(delIndx.pop())
    #         print(newGroup,delIndx)
    #     print("res",result)

    # s = sorted(a)
    # idx = len(a) // 2
    # if len(a) % 2 == 0:
    #     result.append(s[idx - 1])
    # else:
    #     result.append(s[idx])
    #
    # result = set(result)

    return result



print(solution(10,[9,4,4,4,7],[2,10,7,6,3]))
#print(solution(10,[6,3,4,9,2,7,5] ,[4,2,8,2,1,10,3]))