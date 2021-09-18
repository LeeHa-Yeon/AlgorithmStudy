'''
enter	leave	result
[1,3,2]	[1,2,3]	[0,1,1]
[1,4,2,3]	[2,1,3,4]	[2,2,1,3]
[3,2,1]	[2,1,3]	[1,1,2]
[3,2,1]	[1,3,2]	[2,2,2]
[1,4,2,3]	[2,1,4,3]	[2,2,0,2]
'''

def solution(enter, leave):
    n = len(enter)
    answer = [0] * (n+1)
    enter_idx = 0
    leave_idx = 0
    room = set()
    while leave_idx < n:
        if leave[leave_idx] in room:
            room.discard(leave[leave_idx])
            leave_idx += 1
            continue
        if enter[enter_idx] not in room:
            print(room)
            for man in room:
                answer[man] += 1
            answer[enter[enter_idx]] = len(room)
            room.add(enter[enter_idx])
            enter_idx += 1
    return answer[1:]


print(solution([1,4,2,3],[2,1,3,4]))