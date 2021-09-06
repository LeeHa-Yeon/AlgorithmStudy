import sys
T = int(sys.stdin.readline())


for _ in range(T) :
    zeroCnt = [1, 0]
    oneCnt = [0, 1]

    N = int(sys.stdin.readline())

    if N == 0 :
        print("1 0")
    elif N == 1 :
        print("0 1")
    else :
        for i in range(2,N+1) :
            zeroCnt.append(zeroCnt[i-1]+zeroCnt[i-2])
            oneCnt.append(oneCnt[i-1]+oneCnt[i-2])
        print(zeroCnt.pop(),oneCnt.pop())



## 메모리 초과 ㅠㅠ
'''
nList = []

for _ in range(T) :
    N = int(sys.stdin.readline())
    nList.append(N)

dp = [0]*(max(nList)+1)
dp[0] = '0'
dp[1] = '1'

for i in range(2,max(nList)+1) :
    dp[i] = dp[i-1]+dp[i-2]


for n in nList :
    l = list(dp[n])
    zeroCnt = l.count('0')
    oneCnt = l.count('1')

    print(zeroCnt,oneCnt)
'''