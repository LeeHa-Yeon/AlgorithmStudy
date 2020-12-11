# 문제54 : 연속되는 수
# 숫자가 공백으로 구분되어 주어지면 이 숫자가 연속수인지 아닌지 'YES'와 'NO'로 판별하는 프로그램을 작성하세요

# --> abs 활용하


def isSequence(list) :
    for i in range(len(list)-1) :
        if 1 != abs(list[i]-list[i+1]) :
            return False
    return True


numList = list(map(int, input().split()))

if isSequence(numList) :
    print(numList,"----> 연속된 숫자 입니다.")
else :
    print(numList,"----> 연속되지 않았습니다.")기



