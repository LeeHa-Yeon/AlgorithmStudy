from collections import deque
n = int(input())
moneyList = deque()

for _ in range(n) :
    money = int(input())
    if money == 0 :
        moneyList.pop()
        continue
    moneyList.append(money)

if moneyList == [] :
    print(0)
else :
    print(sum(moneyList))