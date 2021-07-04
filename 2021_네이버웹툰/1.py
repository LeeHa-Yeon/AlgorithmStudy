'''
win_lose      result
[1,0,1,0]       1
[0,1,0,1,1,1,0,1,1]    3
'''

def solution(win_lose) :
    if sum(win_lose) == 0 :
        return 0
    cnt = 1

    for i in win_lose :
        if i==1 :
            cnt+=1
        else :
            cnt=1
    return cnt

print(solution([1,0,1,0]))
print(solution([0,1,0,1,1,1,0,1,1]))
print(solution([0,0,0,0]))