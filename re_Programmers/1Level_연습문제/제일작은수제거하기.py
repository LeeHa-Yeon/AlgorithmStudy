'''
arr	return
[4,3,2,1]	[4,3,2]
[10]	[-1]
'''

def solution(arr):
    arr.remove(min(arr))
    if arr == [] :
        return [-1]
    return arr

print(solution([10]))