def solution(n,money) :
    dp = [0]*(n+1)
    dp[0]=1

    for coin in money :
        for price in range(coin,n+1) :
            if price < coin :
                continue
            dp[price]+=dp[price-coin]
    return dp[n]%1000000007

print(solution(5,[1,2,4]))