# 문제 78 : 원형 테이블
# 기린은 중국집에서 친구들과 만나기로 하고 음식을 시켰습니다.
# 음식이 나오고 한참을 기다렸지만 만나기로 한 친구 2명이 오지 않았어요

# 기린은 배가 너무 고파 혼자 음식을 먹기 시작합니다.
# 원형 테이블에는 N개의 음식들이 있습니다.
# 한 개의 음식을 다 먹으면 그 음식의 시계방향으로 K번째 음식을 먹습닏.
# 하지만 아직 오지 않은 친구들을 위해 2개의 접시를 남겨야 합니다

# 마지막으로 남는 음식은 어떤 접시일까요?


def roundTable1(n,k) :
    foodList = [ i for i in range(1,n+1)]
    delIdx = 0

    while len(foodList) > 2 :
        foodList.pop(delIdx)
        delIdx += k-1
        delIdx %= len(foodList)
    return foodList




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

print(f'마지막으로 남는 음식은 {roundTable1(6,4)} 번째 접시 입니다.')
#print(roundTable(3,6))
