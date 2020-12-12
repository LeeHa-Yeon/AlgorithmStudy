# 문제66 : 블럭탑쌓기
# 탑을 쌓기 위해 각 크기별로 준비된 블럭들을 정해진 순서에 맞게 쌓아야 합니다.
# 1. 블럭은 알페벳 대문자로 표기
# 2. 규칙에 없는 블럭이 사용될 수 있습니다.
# 3. 중복된 블럭은 존재하지 않습니다.
# < 입력 >
# 탑 = ["ABCDEF","BCAD","ADEFQRX","BEDFG","EFGHZ"]
# 규칙 = "ABD"
#
# < 출력 >
# ["가능","불가능","가능","가능","가능"]

def solution(allString,rule) :

    answer = []
    for subString in allString :
        subList = []
        for word in subString :
            if word in rule :
                subList.append(word)
        answer.append(isMatch(subList))
    return answer

def isMatch(l) :
    sortList = list(sorted(l))
    if sortList == l :
        return "가능"
    else :
        return "불가능"

topList = ["ABCDEF","BCAD","ADEFQRX","BEDFG","EFGHZ"]
rule = "ABD"
print(solution(topList,rule))





