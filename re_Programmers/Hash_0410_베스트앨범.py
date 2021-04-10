'''
genres	plays	return
["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]
'''
'''
# name:value로 하면 중복으로 인해 가장 높은 value만 추출
# b = { name:value for name, value in zip(a, b) }
'''

def solution(genres, plays):
    albums = []
    initDict = {name: 0 for name, value in zip(genres, plays)}
    max = 0

    # 합쳐서 가장 큰 값을 기준으로
    for i in range(len(genres)) :
        initDict[genres[i]]+=plays[i]

    manyPlaySort = sorted(initDict.items(), key = lambda x:x[1], reverse=True)

    # 장르 내에서 많이 재생된 노래
    manyGenres = [(genres[i], plays[i]) for i in range(len(genres))]
    manyGenresSort = sorted(manyGenres, key=lambda x: (x[0], -x[1]))

    while manyPlaySort :
        standard = manyPlaySort.pop(0)

        for i in range(len(manyGenresSort)) :
            if standard[0] == manyGenresSort[i][0] and max !=2  :
                albums.append(plays.index(manyGenresSort[i][1]))
                max+=1
        max = 0


    return albums

print(solution(['A', 'B', 'A'], [600, 500, 600]))# == [0, 2, 1])  &&&&&&&&&&&&
# print(solution(['A', 'B', 'C', 'D'], [1, 2, 3, 1]))# == [2, 1, 0, 3])  **********
# print(solution(['A', 'A', 'B', 'A'], [2, 2, 2, 3]) )#== [3, 0, 2]) ******
# print(solution(['A', 'A', 'B', 'A'], [5, 5, 6, 5]) )#== [0, 1, 2]) *******
# print(solution(['A', 'A', 'B', 'A', 'B', 'B'], [5, 5, 6, 5, 7, 7]))# == [4, 5, 0, 1]) ******


#
# print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))
# print(solution(['B', 'A'], [500, 600])) # [1, 0])
# print(solution(['B'], [500])) # [0])
# print(solution(['B', 'A'], [600, 500])) # [0, 1])
# print(solution(['A', 'B'], [600, 500])) #[0, 1])
# print(solution(['A', 'A', 'B'], [600, 500, 300]))# == [0, 1, 2])
#
# print(solution(['A', 'B', 'A'], [600, 500, 700]))# == [2, 0, 1])
# print(solution(['A', 'A', 'A'], [600, 500, 700]))# == [2, 0])
# print(solution(['A', 'A', 'A'], [3, 2, 1]) )#== [0, 1])
# print(solution(['classic', 'pop', 'classic', 'classic', 'pop'],
#                [500, 600, 150, 800, 2500]) )#== [4, 1, 3, 0])
# print(solution(['classic'], [2500]) )#== [0])
# print(solution(['A', 'B', 'C'], [1, 2, 3]) )#== [2, 1, 0])
