a,b,c = map(int,input().split(' '))
min  =  a if (a<b) else b
result = min if min<c else c
print(result)