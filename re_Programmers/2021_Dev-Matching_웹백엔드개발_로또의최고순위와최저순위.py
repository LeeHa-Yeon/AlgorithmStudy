'''
lottos	win_nums	result
[44, 1, 0, 0, 31, 25]	[31, 10, 45, 1, 6, 19]	[3, 5]
[0, 0, 0, 0, 0, 0]	[38, 19, 20, 40, 15, 25]	[1, 6]
[45, 4, 35, 20, 3, 9]	[20, 9, 3, 45, 4, 35]	[1, 1]
'''

def solution(lottos, win_nums):
    inconsisSet = set(win_nums) - set(lottos)
    correctCnt = len(win_nums) - len(inconsisSet)
    zeroCnt = lottos.count(0)
    high,low = correctCnt+zeroCnt,correctCnt

    if high >= 6 :
        highest = 1
    elif high <= 1 :
        highest = 6
    else :
        highest = 7-high

    if low >= 6 :
        lowest = 1
    elif low <= 1 :
        lowest = 6
    else :
        lowest = 7-low

    return [highest,lowest]

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]))