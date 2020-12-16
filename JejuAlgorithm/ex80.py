# 문제 80 : 순회하는 리스트

from itertools import combinations

inputList = ['ㄱ','ㄴ','ㄷ','ㄹ']

l = list(combinations(inputList,3))
resultList = []

for i in l :
    str = ''
    for j in i :
        str+=j
    resultList.append(str)


print(resultList,len(resultList),sep="\n")