# 문제42 : 2020년
#
# 2020년 1월 1일은 수요일입니다. 2020년 a월b일은 무슨 요일일까요?
# 두 수  a,b를 입력받아 2020년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.
# 요일의 이름은 일요일부터 토요일까지 각각 sun,mon,tue,wed,thu,fri,sat입니다.
# ( 예를 들어 a = 5, b = 24라면 5월 24일은 일요일이므로, 문자열 sun를 반환하세요 )
#
# 제한 조건
# 2020년은 윤년입니다.
# 2020년 a월 b일은 실제로 있는 날입니다.
# (13월 26일이나 2월 45일 같은 날짜는 주어지지 않습니다.)

import datetime
def solution(monday,day) :
    weekList = ['mon','tue','wed','thu','fri','sat','sun']
    weekIndex = datetime.date(2020,monday,day).weekday()
    return weekList[weekIndex]

a,b = map(int,input().split(' '))
print(solution(a,b))





''' import datetime

timedelta(기간 표시) :  주, 일, 시, 분, 초, 마이크로 초, 밀리 초를 인자로 받습니다.
date(날짜) : 연, 월, 일 데이터를 인자 받습니다. / 오늘 날짜 얻고싶다면 today() 메소드 사용
          : date 클래스의 isoformat() 메서드는 date 객체를 YYYY-MM-DD 형태의 문자열로 변환해
          : date 클래스의 fromisoformat() 메서드는 YYYY-MM-DD 형태의 문자열을 date 객체로 변환
          : date 클래스의 weekday()와 isoweekday() 메서드는 해당 날짜가 무슨 요일인지를 파악하기 위해서 사용됩니다. 
            두 메서드는 차이는 weekday()에서는 월요일이 0으로 시작하는 반면에, isoweekday()에서는 월요일이 1로 시작한다는 점입니다.

import datetime
datetime.date(year,month,day) -> ex) 2020 - 08 - 03 return
datetime.time(hour,min,secend) -> ex) 16:04:55 return
.weekend() -> 0~ 6 return -> 월 ~ 일

'''