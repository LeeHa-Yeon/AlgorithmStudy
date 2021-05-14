'''
orders	course	result
["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	[2,3,4]	["AC", "ACDE", "BCFG", "CDE"]
["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	[2,3,5]	["ACD", "AD", "ADE", "CD", "XYZ"]
["XYZ", "XWY", "WXA"]	[2,3,4]	["WX", "XY"]
'''


from itertools import combinations
from collections import Counter
def solution(orders, course):

    orders_combi,orders_temp ,result = [],[],[]

    # orders의 각 문자열을 조합하기전에 정렬시켜 문자열상태로 합치기
    orders_sort = list(map(list,orders))
    for i in orders_sort :
        i.sort()
        orders_temp.append("".join(i))

    # 코스 개수별로 조합을 만들어서 모든 경우의수를 만든 후
    # Counter로 묶어서 함께 주문된 단품메뉴의 개수 알기
    for i in orders_temp :
        for j in course :
            orders_combi.extend(list(map("".join,combinations(i,j))))
    orders_combi = Counter(orders_combi)

    # 각 코스별로 많이 주문한 메뉴를 선별
    for i in course :
        course_orders = []
        for j in orders_combi.items() :
            if len(j[0]) == i and j[1] > 1 :
                course_orders.append(list(j))
        if course_orders != [] :
            course_orders_sorted = sorted(course_orders, key=lambda x: x[1], reverse=True)
            standard = course_orders_sorted[0][1]
            for j in course_orders_sorted :
                if standard != j[1] :
                    break
                else :
                    result.append(j[0])

    return list(sorted(result))

# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))