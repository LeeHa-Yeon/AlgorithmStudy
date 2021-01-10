'''
numbers	            return
[6, 10, 2]	        6210
[3, 30, 34, 5, 9]	9534330
'''


def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key=lambda x: x * 3,reverse=True)

    if int(''.join(numbers)) == 0 :
        return '0'
    return ''.join(numbers)

print(solution([3, 30, 34, 5, 9]))



''' 시간초과
from itertools import permutations

def solution(numbers):
    numbers = list(map(str,numbers))
    perList= list(map(''.join, permutations(numbers,len(numbers))))
    perList = list(map(int,perList))
    return str(max(perList))

print(solution([6, 10, 2]))

---------------------------------------------------------------------------

from itertools import permutations

def solution(numbers):
    numbers = list(map(str,numbers))
    perList= list(map(''.join, permutations(numbers,len(numbers))))
    perList.sort(reverse=True)

    return str(perList[0])

print(solution([6, 10, 2]))


'''