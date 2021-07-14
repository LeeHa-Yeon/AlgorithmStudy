from math import gcd
def solution(arr):
    x = arr[0]
    for y in arr[1:] :
        x = x*y // gcd(x,y)
    return x