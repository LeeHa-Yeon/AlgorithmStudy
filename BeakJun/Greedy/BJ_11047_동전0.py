n,k = map(int,input().split(' '))
coinList = []
cnt = 0

for i in range(n) :
    coinList.append(int(input()))

for coin in range(0,len(coinList)) :
    if coinList[-coin] < k :
        cnt+=k//coinList[-coin]
        k%=coinList[-coin]
    else :
        continue
print(cnt)

'''

n = int(input())
coin = 1000-n
changeList=[500,100,50,10,5,1] # 거스름돈 종류
cnt=0

for change in changeList:
  cnt+=coin//change
  coin%=change

print(cnt)
'''