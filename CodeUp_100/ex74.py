n = int(input())
l = list()

for i in range(n+1) :
    if i % 2 == 0 :
        l.append(i)
print(sum(l))