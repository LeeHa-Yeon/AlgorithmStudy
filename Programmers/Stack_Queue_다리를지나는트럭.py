'''
bridge_length	weight	truck_weights	return
2	10	[7,4,5,6]	8
100	100	[10]	101
100	100	[10,10,10,10,10,10,10,10,10,10]	110




경과 시간	다리를 지난 트럭	다리를 건너는 트럭	대기 트럭
0	[]	[]	[7,4,5,6]
1~2	[]	[7]	[4,5,6]
3	[7]	[4]	[5,6]
4	[7]	[4,5]	[6]
5	[7,4]	[5]	[6]
6~7	[7,4,5]	[6]	[]
8	[7,4,5,6]	[]	[]

'''

from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge_trucks = [0]*bridge_length # 이걸 deque로 바꾼후 pop(0)대신 popleft() 사용하면 더 빠를 줄 알고 사용했는데 오히려 시간초과
    time = 0

    while bridge_trucks :
        bridge_trucks.pop(0)
        time+=1
        if truck_weights :
            if sum(bridge_trucks)+truck_weights[0] <= weight :
                bridge_trucks.append(truck_weights.popleft())
            else :
                bridge_trucks.append(0)
    return time


print(solution(100,100,[10]))
