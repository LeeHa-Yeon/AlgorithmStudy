# Union of Computer Programming Contest club contest
# University Computer Programming

string = input()
b = 'UCPC'
a = ''

# a = CUPC

# 대문자로 함축시키는 작업
for i in string :
    if i.isupper() :
        a+=i

# UCPC 순서대로 있는지 확인

dp=[["" for _ in range(len(b))]for _ in range(len(a))]

for i in range(1,len(a)):
    for j in range(1,len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + a[i]
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
               dp[i][j]=dp[i-1][j]
            else:
               dp[i][j]=dp[i][j-1]




if 'UCPC' in a:
    print("I love UCPC")
else :
    print("I hate UCPC")