# 500엔, 100엔, 50엔, 10엔, 5엔, 1엔

n = int(input())
coin = 1000-n
changeList=[500,100,50,10,5,1] # 거스름돈 종류
cnt=0

for change in changeList:
  cnt+=coin//change
  coin%=change

print(cnt)