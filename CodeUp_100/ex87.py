# 1 -1 3 -5 11 -21 43

a,m,d,n = map(int,input().split(' '))

result = a
for _ in range(n-1) :
    result = result*m+d

print(result)