# 문제 : 내장함수 응용하기
# 0부터 1000까지 1의 개수를 세는 프로그램을 만들려고 합니다.
# 예를 들어 0부터 20까지 1의 개수를 세어본다면 1,10,11,12,13,14,15,16,17,18,19에 각 1이 들어가므로 12개의 1이 있게 됩니다.
# 11은 1이 2번 들어간 셈이다.
# 그렇다면 0부터 1000까지 수에서 1은 몇번이나 들어갔을까요? 출력해주세요

n = 20

print('------> 방법 1 ')

s = ''
for i in range(n+1) :
    s+=str(i)

print(s.count('1'))


print('------> 방법 2 ')

s1 = str(list(range(n+1)))
print(s1.count('1'))