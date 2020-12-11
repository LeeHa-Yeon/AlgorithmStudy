# 문제50 : 버블 정렬 구하기

# 버블 정렬은 두 인접한 원소를 검사하여 정렬하는 방법을 말합니다.
# 시간 복잡도는 느리지만 코드는 단순하기 때문에 자주 사용합니다.

# 42385

def bubble(n,data) :
    for i in range(1,n) :
        for j in range(n-i) :
            if data[j] > data[j+1] :
                data[j] , data[j+1] = data[j+1], data[j]
    for i in range(n) :
        print(data[i], end=" ")


data = list(map(int,input().split(' ')))
bubble(len(data),data)