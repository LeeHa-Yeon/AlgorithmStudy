# 문제65 : 변형된 리스트
# a = [1,2,3,4]
# b = [a,b,c,d]
# 이런 리스트가 있을 때 [[1,a],[b,2],[3,c],[d,4]] 이런 식으로 a,b 리스트가 번갈아가면서 출력되게 해주세요 2열 ,4행

print("-------> 방법 1 ")

a = [1,2,3,4]
b = ['a','b','c','d']
rowResult = []

for i in range(len(a)) :
    # append -> 하나의 argument(독립변수)만 취함
    if i%2 ==0 :
        rowResult.append([a[i],b[i]])
    else :
        rowResult.append([b[i],a[i]])

print(rowResult)

print("-------> 방법 2 ")

count = 0
rowResult.clear()

for i,j in zip(a,b):
    if count%2 == 0 :
        rowResult.append([i,j])
    else :
        rowResult.append([j,i])
    count+=1

print(rowResult)
'''
- 2중 리스트 

3열 2행 만들기 

1. [[0 for col in range(3)] for row in range(2)]
2. [[0]*3 for row in range(2)]
3. [[0]*3]*2

'''
