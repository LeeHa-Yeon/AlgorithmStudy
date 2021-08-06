a,b = map(int,input().split(' '))
aSet = set()
bSet = set()

for i in range(a) :
    aSet.add(input())
for i in range(b) :
    bSet.add(input())

answer = sorted(aSet & bSet)

print(len(answer))
for i in answer :
    print(i)