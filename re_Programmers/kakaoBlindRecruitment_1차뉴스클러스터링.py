'''
3:50 ~
str1	str2	answer
FRANCE	french	16384
handshake	shake hands	65536
aa1+aa2	AAAA12	43690
E=M*C^2	e=m*c^2	65536

'''

from collections import Counter

def solution(str1, str2):
    aSet = []
    bSet =[]

    # 두개씩 쪼개기
    # 단, 숫자,특수문자,공백 제거한 문자열만
    for i in range(len(str1)-1) :
        aElement = str1[i:i+2]
        if aElement.isalpha() :
            aSet.append(aElement.lower())

    for i in range(len(str2)-1) :
        bElement = str2[i:i + 2]
        if bElement.isalpha():
            bSet.append(bElement.lower())

    # 만약 둘다 공집합일 경우
    if aSet == [] and bSet == [] :
        return int(1*65536)

    # 그냥 합집합, 교집합 한거
    union = len(list(set(aSet) | set(bSet)))
    intersection = len(list(set(aSet) & set(bSet)))


    #저기에 중복된 값을 추가해서 넣어야됨
    aCnt = Counter(aSet)
    bCnt = Counter(bSet)
    overlap = []


    for k, v in aCnt.items():
        if v != 1:
            overlap.append([k,v])


    for k, v in bCnt.items():
        if v != 1 :
            overlap.append([k, v])

    overlap.sort()

    for p1, p2 in zip(overlap.copy(), overlap[1:].copy()):
        if p1[0] == p2[0] :
            if p1[1] < p2[1] :
                union+=(p2[1]-1)
                intersection+=(p1[1]-1)
            else :
                union += (p1[1] - 1)
                intersection += (p2[1] - 1)
            idx = overlap.index([p1[0],p1[1]])
            del overlap[idx]
            idx = overlap.index([p2[0], p2[1]])
            del overlap[idx]

    for i in overlap :
        union+=(i[1]-1)

    return int(intersection/union*65536)

# print(solution("FRANCE","french"))
# print(solution("handshake","shake hands"))
print(solution("aa1+aa2","AAAA12"))
# print(solution("E=M*C^2","e=m*c^2"))
# print(solution("aaabbbb", "aaaabbb"))
# print(solution('abcccc','cccdefff'))
# print(solution('cccdefff','abcccc'))
# print(solution("ABDDD", "DDEFGHH"))
# print(solution("AACCC", "A A A A A C C C C"))
# print(solution("AAbbaa_AA"," BBB"))
# print(solution("CCDEFGHH", "ABCCC"))
# print(solution("FRANCE", "french"))
# print(solution("handshake", "shake hands"))
# print(solution("aa1+aa2", "AAAA12"))
# print(solution("E=MC2", "e=mc2"))