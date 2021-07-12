
'''
genres	plays	return
["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]

'''


def solution(genres, plays):
    albums = []
    initDict = {name: 0 for name in genres}

    # 합쳐서 가장 큰 값을 기준으로
    for i in range(len(genres)) :
        initDict[genres[i]]+=plays[i]

    manyPlaySort = sorted(initDict.items(), key = lambda x:x[1], reverse=True)

    # 장르 내에서 많이 재생된 노래
    manyGenres = [(genres[i], plays[i]) for i in range(len(genres))]
    manyGenresSort = sorted(manyGenres, key=lambda x: (x[0], -x[1]))

    while manyPlaySort :
        standard = manyPlaySort.pop(0)
        max = 0
        for i in range(len(manyGenresSort)) :
            if standard[0] == manyGenresSort[i][0] and max !=2  :
                # 고유 번호가 낮은 노래 먼저 수록
                idx = manyGenres.index((manyGenresSort[i][0],manyGenresSort[i][1]))
                manyGenres[idx] = 0
                albums.append(idx)
                max+=1

    return albums


# print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))
# print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 500, 800, 2500]))
print(solution(["A", "A", "B", "A", "B", "B", "A", "A", "A", "A"],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
# print(solution(["classic", "pop", "classic", "classic", "jazz", "pop", "Rock", "jazz"],[500, 600, 150, 800, 1100, 2500, 100, 1000]))
# print(solution(["A","A","B","A"], [5,5,6,5]))