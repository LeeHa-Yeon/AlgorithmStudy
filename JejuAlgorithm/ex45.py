# 문제 : time함수 사용하기
# python의 모듈 중 하나인 time 모듈은 1970년 1월 1일 0시 0분 0초 이후로부터 지금까지 흐른 시간을 초단위로 반환합니다.
# 이를 이용하여 현재 연도(2019)를 출력해보세요

import time

now_year = time.strftime('%Y',time.localtime(time.time()))
print(now_year)



'''
import time
time.strftime('포멧',시간객체)

포멧 : %A 요일 , %Y 연 , %B 문자 월 / %m 숫자 월 , %d 일 , %c 날짜와 시간
시간객체 : localtime(time.time())
'''