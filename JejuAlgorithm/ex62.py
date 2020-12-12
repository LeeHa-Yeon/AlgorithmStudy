# 문제62 : 20190923출력하기
# < 기준 >
# 1. 코드 내에 숫자가 없어야 합니다.
# 2. 파일 이름이나 경로를 사용해서는 안됩니다.
# 3. 시간, 날짜 함수를 사용해서는 안됩니다.
# 4. 에러 번호 출력을 이용해서는 안됩니다.
# 5. input을 이용해서는 안됩니다.


s = 'abbcccddddddddd'

zero = s.count('g')
one = s.count('a')
two = s.count('b')
three = s.count('c')
nine = s.count('d')

print(two,zero,one,nine,zero,nine,two,three,sep='')