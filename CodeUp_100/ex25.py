import math
def math1(n,i) :
    a = int(math.pow(10,i))
    return n*a


n = int(input())
l = list()
for i in range(len(str(n))) :
    a = n % 10   # 4, 5, 2, 5, 7
    n = int(n/10)
    l.append(math1(a,i))

for j in range(len(l)-1,-1,-1) :
    print([l[j]])