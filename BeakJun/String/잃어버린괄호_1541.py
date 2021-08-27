import re
from collections import deque

expression = input()

numbers = deque(re.findall("\d+",expression))
operators = re.findall("\W",expression)

answer = numbers.popleft()
number = 0

for first,second in zip(operators,operators[1:]) :

    if first=='+' and second=='-' :
        number = -(number)
        answer+=number
        number = 0
    elif first=='-' and second=='+' :
        number = numbers.popleft()
    elif first=='-' and second=='-' :
        answer-=numbers.popleft()
    else :
        number+=numbers.popleft()





print(numbers,operators)