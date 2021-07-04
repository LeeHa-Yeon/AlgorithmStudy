'''
play_list   listen_time   result
[2,3,1,4]     3            3
[1,2,3,4]     5            4
[1,2,3,4]     20           4


1. 가장 작은 수(여기선 1)를 기점으로 양옆
    - 가장 작은 수의 인덱스를 먼저 찾기
2. 양옆 중 더 작은 수쪽에 남은 시간 쓰기


'''

from itertools import chain, repeat
def solution(play_list,listen_time) :
    minIdx = play_list.index(min(play_list))
    listen_time = listen_time-play_list[minIdx]
    cnt = 1
    orgin_playList_len =len(play_list)

    if len(play_list) <= listen_time :
        play_list = list(chain.from_iterable(repeat(play_list,listen_time//orgin_playList_len+1)))

    if listen_time != 0 :
        before,after = play_list[minIdx-1],play_list[minIdx+1]
        listen_time -= 1
        cnt += 1
        i = 0
        if before < after :
            # before쪽 반복문
            while listen_time>0 and orgin_playList_len > cnt:
                listen_time = listen_time-play_list[minIdx-1-i]
                i+=1
                cnt+=1

        else :
            # after쪽 반복문
            while listen_time >0 and orgin_playList_len > cnt:
                listen_time = listen_time-play_list[minIdx+1+i]
                i+=1
                cnt+=1
    else :
        return cnt

    return cnt

print(solution([2,3,1,4],3))
print(solution([1,2,3,4],5))
print(solution([1,2,3,4],20))
