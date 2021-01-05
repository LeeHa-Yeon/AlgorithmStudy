n = int(input())
hills = map(int,input().split(' '))

maxHill = 0
cnt = 0
result = 0

for hill in hills :
    if hill > maxHill :
        maxHill = hill
        cnt = 0
    else :
        cnt+=1
    result = max(result,cnt)


print(result)