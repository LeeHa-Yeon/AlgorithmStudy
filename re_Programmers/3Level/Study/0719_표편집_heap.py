import heapq

def inverse(num):
    return -num

def solution(n, k, cmds):
    # 최대힙은 현재위치 전까지
    # inverse를 하는 이유는
    # 최대힙은 heapq 모듈에는 없어서 최소힙을 약간 응용해야 하는데 힙에 튜플의 원소를 추가하거나 삭제하면 튜플 내에서는 맨 앞에 있는 값을 기준으로 최소 힙이 구성되므로
    # -를 붙여 넣으면 최대힙이 만들어지고
    # 이를 이용하는 이유는
    max_heap = list(map(inverse, range(k)))
    # 최소힙은 현재위치부터 나머지
    min_heap = list(range(k, n))
    heapq.heapify(max_heap)
    heapq.heapify(min_heap)

    # 처음 표의 상태는 모두 'O'로 초기화
    table = ['O' for _ in range(n)]
    # Z로 순차적으로 삭제된 인덱스를 알아내기 위해 deleted_stack 생성 -> append,pop 사용
    deleted_stack = []

    for cmd in cmds:
        command = cmd.split()
        command1 = command[0]

        # U 과 D
        if command1 == "D":
            num = int(command[1])
            for _ in range(num):
                # 현재위치가 내려가니까 min에 있는 값을 내려간 갯수만큼 max로 옮기기
                # 현재위치가 바뀜
                heapq.heappush(max_heap, -heapq.heappop(min_heap))

        elif command1 == "U":
            num = int(command[1])
            for _ in range(num):
                # 현재위치가 올라가니까 max에 있는 값을 올라간 갯수만큼 min로 옮기기
                # 현재위치가 바뀜
                heapq.heappush(min_heap, -heapq.heappop(max_heap))

        # C 와 Z
        elif command1 == 'C':
            # 현재위치 값(최소힙의 맨 앞의 값)을 pop을 통해 delete_num로 지정 후 delete_stack에 넣어두기
            delete_num = heapq.heappop(min_heap)
            deleted_stack.append(delete_num)
            table[delete_num] = 'X'
            # 현재 위치가 마지막 행이였을 경우 삭제 시 내려갈 칸이 없으므로
            # 한칸 올라가야한다 => 즉 현재 위치는 여전히 마지막 행(가장 큰 값)이여야 하므로 다시 최대힙에 있는 것을 pop해서 최소힙에 넣기
            # 최소힙에 있는 값이 현재 위치
            if len(min_heap) == 0:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif command1 == 'Z':
            # 스택은 후입선출로 delete_stack은 마지막에 삭제된 값이 pop으로 나옴
            restore_num = deleted_stack.pop()
            table[restore_num] = 'O'
            # 복원할 값이 현재 위치의 값보다 작다면 최대힙에 넣어야 되고
            if min_heap[0] > restore_num:
                heapq.heappush(max_heap, -restore_num)
            # 크다면 최소힙에 넣어야됨
            else:
                heapq.heappush(min_heap, restore_num)

    # list형태를 문자열로 join하여 리턴
    return ''.join(table)


# print(solution(8,2,["D 5","C","C","U 1","C"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
# print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
