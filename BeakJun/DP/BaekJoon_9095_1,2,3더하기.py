input_num = int(input())
inputList = []
for _ in range(input_num) :
    inputList.append(int(input()))

dp = [0]*(max(inputList)+1)
for i in range(1,max(inputList)+1) :
    if i == 1 or i == 2 :
        dp[i] = i
    elif i == 3 :
        dp[i] = i+1
    else:
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

for i in inputList :
    print(dp[i])