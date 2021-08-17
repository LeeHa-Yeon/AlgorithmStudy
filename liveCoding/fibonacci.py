def fibo(n) :
    if n == 0 :
        return 0
    elif n < 3 :
        return 1
    else :
        return fibo(n-1)+fibo(n-2)

def fibo1(n) :
    list = [0,1,1]

    for i in range(3,n+1) :
        list.append(list[i-1]+list[i-2])

    return list[n]

def fibo2(n) :
    dp = [0]*(n+1)
    dp[1] = 1
    for i in range(2,n+1) :
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]

print(fibo2(6))

