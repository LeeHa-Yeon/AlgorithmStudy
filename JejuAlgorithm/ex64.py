# 문제64 : 이상한 엘레베이터
# 정량N에 정확히 맞춰야만 움직이는 화물용 엘베
# 화물은 7kg,3kg 두 가지이며 팔이 아픈 은후는 가장 적게 화물을 옮기고 싶습니다.
# 예를 들어 정량이 24kg이라면 3kg 8개 옮기는 것 보단
# 7kg 3개, 3kg 1개 즉 4개로 더 적게 옮길 수 있습니다.
# 입력 : 정량 N이 입력됩니다.
# 출력 : 가장 적게 옮길 수 있는 횟수를 출력합니다
#     : 만약 어떻게 해도 정량이 N이 되지 않는다면 -1을 출력

weight = int(input())
big = 7
small = 3
count = 0

bigDivTuple = divmod(weight,big)
count+=bigDivTuple[0]
bigMod = bigDivTuple[1]

smallDivTuple = divmod(bigMod,small)
# print(*(divmod(24,7))) #unpacking
count+=smallDivTuple[0]

if smallDivTuple[1] == 0 :
    print(count)
else :
    print(-1)


'''
- divmod(a,b)
  : 두 숫자를 나누어 몫과 나머지를 tuple로 반환하는 함수
  : b에 0을 넣지 않도록 주의 
  : 큰 숫자를 이용할 경우에는 이 메소드가 좋음 ( 단, 작은 숫자의 경우엔 a//b , a%b 를 이용하는 것이 좋음 )
'''
