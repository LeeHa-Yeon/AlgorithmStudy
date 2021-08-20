from collections import deque

n = int(input())
if n== 1:
    print(1)
else :
    cardList = [i for i in range(1,n+1)]
    cardList = deque(cardList)
    while True:
        cardList.popleft()
        if len(cardList) == 1:
            print(cardList[0])
            break
        cardList.append(cardList.popleft())