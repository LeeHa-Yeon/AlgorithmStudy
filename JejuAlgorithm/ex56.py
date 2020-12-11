# 문제56 : 딕셔너리의 함수 응용
# 다음의 딕셔너리가 주어졌을 때 한국의 면적과 가장 비슷한 국가와 그 차이를 출력하세요.

nationWidth = {
    'korea' : 220877,
    'Rusia' : 1709842,
    'China' : 9596961,
    'France' : 543965,
    'England' : 242900
}

stardardValue = nationWidth.get('korea')  # 220877
nationWidth.pop('korea')
keyList = nationWidth.keys()   # ['korea','Rusia','China','France','England']
valueList = nationWidth.values()   # [220877, 1709842, 9596961, 543965, 242900]
itemList = nationWidth.items()
minGap = max(valueList)

for itemTuple in itemList :
    nationAbs = abs(stardardValue - itemTuple[1])
    if minGap > nationAbs :
        minGap = nationAbs
        resultName = itemTuple[0]

print(resultName,minGap)







# standardValue = nationWidth.get('korea')
# tupleNation = nationWidth.items()
# country = ''
#
#
# for i in nationWidth :
#     if i != 'korea' :
#         difference = abs(standardValue - nationWidth[i])
#         nationWidth[i] = difference
#
# for i in tupleNation:
#     if i[1] == min(nationWidth.values()):
#         country = i[0]
#
#
# print(country,min(nationWidth.values()))


'''
1. Tuple
tuple = [(key1,value1),(key2,value2),(key3,value3),(key4,value4)]
element = (key,value) 
element[0] = key
element[1] = value

2. Dictionary
.pop(key) -> key에 해당하는 원소를 삭제, 삭제한값을 return. ( key값이 없으면 오류 )
.get(key,default_value) -> key의 값을 리턴한다. 없으면 디폴트값을 리턴 (디폴트값이 없으면 무시)
.values() -> dictionary의 value 값들을 list로 변환
.keys() -> dictionary key 값들을 list로 변환 
.items() -> dictionary를 각각의 tuple로 변환 -> (키,값) 

- 특정값을 찾기  : 키를 이용한다. 리스트와 달리 인덱스는 지원하지 않는다. 
dic[키] = 값

- dic1, dic2 합치기 (단, 중복의 경우 dic2의 값으로 변경 )
dic1.update(dic2) 

- 추가하기 : 새로운 값을 추가하려면 새로운 키와 값을 할당하면 된다. 
dic[새로운 키] = 값

- 특정값 삭제 
del dic[]

- 모두 삭제하기
dic.clear()

'''