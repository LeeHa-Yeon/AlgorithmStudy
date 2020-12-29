point = [1,1,3,2,5]
#point = [5,2,3,1,2,5]
dish = 1

def solution(point,dish) :
    dish-=1
    cnt = 0
    pointSort = sorted(point)

    while True :
        print(dish)
        firstDish = point.pop(0)
        if pointSort[0] == firstDish :
            if dish == 0 :
                break
            dish-=1
            pointSort.pop(0)
        else :
            point.append(firstDish)
            dish = len(point)-1 if dish == 0 else dish - 1
        cnt+=1
    return cnt

print("cnt : ",solution(point,dish))