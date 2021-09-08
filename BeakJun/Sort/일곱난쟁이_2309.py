import sys
from itertools import combinations

dwarfList = []

for _ in range(9) :
    dwarfList.append(int(sys.stdin.readline()))

l = combinations(dwarfList,7)

for i in l :
    if sum(i) == 100 :
        answer = list(i)

answer.sort()

for i in range(7) :
    print(answer[i])

