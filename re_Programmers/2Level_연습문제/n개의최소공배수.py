'''
arr	result
[2,6,8,14]	168
[1,2,3]	6
'''

from math import gcd
def lcm(x,y) :
    return x*y//gcd(x,y)
def solution(arr):
    while len(arr) != 1 :
        arr.append(lcm(arr.pop(0),arr.pop(0)))
    return arr.pop()

print(solution([2,6,8,14]))