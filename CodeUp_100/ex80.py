r,b,g = map(int,input().split(' '))

for i in range(r) :
    for j in range(b) :
        for k in range(g) :
            print(i,j,k)
print(r*b*g)