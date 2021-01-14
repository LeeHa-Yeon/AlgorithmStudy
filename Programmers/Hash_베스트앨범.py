'''
genres	                                plays	                    return
[classic, pop, classic, classic, pop]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]
'''


from collections import Counter

def solution(genres, plays):
    answer = sorted(list(zip(genres, plays)))
    dic = dict(zip(genres,[0]*len(genres)))

    # 각 장르별 합산  {'classic': 1450, 'pop': 3100 }
    for i,j in answer :
        dic[i]+=j

    # ['pop', 'classic']
    dic = sorted(dic,key=lambda x:x[1],reverse=True)

    





    return 0


print(solution(['classic','pop','classic','classic','pop'],[500, 600, 150, 800, 2500]))



'''
 answer = sorted(list(zip(genres,plays))) # [('classic', 150), ('classic', 500), ('classic', 800), ('pop', 600), ('pop', 2500)]
    genres.sort()
    standard = answer[0][0]
    result = []
    for i,j in zip(genres,plays) :
        answer.



    # for i in range(len(answer)) :
    #     if standard == answer[i][0] :
    #         sum+=answer[i][1]
    #         if i == len(answer)-1 :
    #             result.append(sum)
    #             result1.append(standard)
    #     else :
    #         result.append(sum)
    #         result1.append(standard)
    #         standard = answer[i][0]
    #         sum = answer[i][1]
    #
    # genresSum = sorted(list(zip(result,result1)),reverse=True)
    #
    # for i in genresSum :
    #     print(i[1])
    #
    #
    # print(genresSum)
'''