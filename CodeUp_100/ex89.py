# 안되는 코드 -> 이유는 모르겟음
# n = int(input())
# l = list(map(int,input().split(' ')))
# result = list()
#
# for i in range(1,24) :
#     print(l.count(i),end=' ')


n=int(input())
b=input().split()
arr=list()

for i in range(24) :
    arr.append(0)

for i in range(n) :
    arr[int(b[i])]+=1

for i in range(1, 24) :
    print(arr[i], end=' ')