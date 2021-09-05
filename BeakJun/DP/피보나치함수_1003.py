import sys
T = int(sys.stdin.readline())
nList = []

for _ in range(T) :
    N = int(sys.stdin.readline())
    nList.append(N)

dp = [0]*(max(nList)+1)
dp[0] = 0
dp[1] = 1

print(dp)

for i in range(2,max(nList)+1) :
    dp[i] = dp[i-1]+dp[i-2]

print(dp[max(nList)])