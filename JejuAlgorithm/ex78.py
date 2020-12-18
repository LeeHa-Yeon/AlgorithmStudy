# 문제 78 : 원형 테이블


def test() :
    foodList = [1,2,3,4,5]

    for i in foodList :
        print(i)


def roundTable(m,n) :
    foodList = [i for i in range(1,n+1)]
    idx = 0

    while len(foodList) > 2 :
        # 첫번째 음식을 먹음
        foodList.pop(idx)
        # 요소의 삭제와 함께 인덱스 1을 빼주는 게 포인트
        idx+=(m-1)
        if idx > len(foodList) -1 :
            idx -= len(foodList)
            print(idx)
            foodList.pop(idx)
            idx-=1
    return foodList

test()
#print(roundTable(3,6))
