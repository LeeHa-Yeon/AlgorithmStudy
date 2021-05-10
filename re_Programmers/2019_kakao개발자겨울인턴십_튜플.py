'''
s	result
"{{2},{2,1},{2,1,3},{2,1,3,4}}"	[2, 1, 3, 4]
"{{1,2,3},{2,1},{1,2,4,3},{2}}"	[2, 1, 3, 4]
"{{20,111},{111}}"	[111, 20]
"{{123}}"	[123]
"{{4,2,3},{3},{2,3,4,1},{2,3}}"	[3, 2, 4, 1]
'''

import re
def solution(s):
    temp = []
    answer = []
    l = s.split('},')

    # 임시리스트에 각 집합을 추출하여 넣기
    for i in l :
        a = re.findall('\d+',i)
        # ['1', '2', '3']
        # ['2', '1']
        # ['1', '2', '4', '3']
        # ['2']
        temp.append(a)

    # 길이순으로 정렬
    # [['2'], ['2', '1'], ['1', '2', '3'], ['1', '2', '4', '3']]
    temp.sort(key=len)

    # 그 리스트에 따라서 answer에 넣기
    for i in temp :
        while i :
            p = i.pop()
            if p in answer :
                continue
            else :
                answer.append(p)


    return list(map(int,answer))

print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
