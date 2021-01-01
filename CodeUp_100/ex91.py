n = int(input())
arr = list(map(int,input().split(' ')))
min = arr[0]

for i in range(n) :
    if min > arr[i] :
        min = arr[i]

print(min)