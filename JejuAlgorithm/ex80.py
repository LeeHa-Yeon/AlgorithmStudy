# 문제 80 : 순열과 조합

# 조합이란 원소들을 조합하여 만들 수 있는 경우의 수이며 원소의 순서는 신경쓰지 않습니다.
# 순열이란 원소의 값이 같더라도 순서가 다르면 서로 다른 원소로 취급하는 선택법입니다.
#
# 한글의 자모 24자 중 자음은 총 14개 입니다.
# 이 중 입력받은 자음을 n개를 선택하여 나올 수 있는 모든 조합과 조합의 수를 출력하고 싶습니다.
#
# 나올 수 있는 모든 조합을 아래와 같이 출력해주세요.
#
# 요구조건
# 1. 첫 줄에 선택할 한글 자음이 주어집니다.
# 2. 두번째 줄에 조합의 수가 주어집니다.
# 3. 주어진 조합의 수에 따라 조합과 조합의 수를 출력해주세요.
#
# 입력
# ㄱ,ㄴ,ㄷ,ㄹ
# 3
#
# 출력
# [‘ㄱㄴㄷ’,’ㄱㄴㄹ’,’ㄱㄷㄹ’,’ㄴㄷㄹ’]
# 4

from itertools import combinations

def solution(list,n) :
    answer = []
    combiList = combinations(list,n)

    for combiTuple in combiList :
        totalStr = ''
        for combiWord in combiTuple :
            totalStr += combiWord
        answer.append(totalStr)

    return answer


list1 = ['ㄱ','ㄴ','ㄷ','ㄹ']
n = 3
print(f'조합된 리스트 : {solution(list1,n)} \n총 개수 : {len(solution(list1,n))}')







# inputList = ['ㄱ','ㄴ','ㄷ','ㄹ']
#
# l = list(combinations(inputList,3))
# resultList = []
#
# for i in l :
#     str = ''
#     for j in i :
#         str+=j
#     resultList.append(str)
#
#
# print(resultList,len(resultList),sep="\n")