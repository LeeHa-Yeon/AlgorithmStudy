# 문제34 : sort 구현하기
# 키가 주어지면 순서대로 제대로 섰는지 확인하는 프로그램을 작성해보자

height = list(map(int , input().split(' ')))

if height == sorted(height) :
    print("YES")
else :
    print("No")