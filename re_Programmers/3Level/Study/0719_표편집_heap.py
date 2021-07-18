import heapq

def inverse(num):
    return -num

def solution(n, k, cmds):
    max_heap = list(map(inverse, range(k)))
    min_heap = list(range(k, n))
    heapq.heapify(max_heap)
    heapq.heapify(min_heap)

    table = ['O' for _ in range(n)]
    deleted_stack = []

    for cmd in cmds:
        command = cmd.split()
        command1 = command[0]

        # U 과 D
        if command1 == "D":
            num = int(command[1])
            for _ in range(num):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
        elif command1 == "U":
            num = int(command[1])
            for _ in range(num):
                heapq.heappush(min_heap, -heapq.heappop(max_heap))

        # C 와 Z
        elif command1 == 'C':
            delete_num = heapq.heappop(min_heap)
            deleted_stack.append(delete_num)
            table[delete_num] = 'X'
            if len(min_heap) == 0:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif command1 == 'Z':
            restore_num = deleted_stack.pop()
            table[restore_num] = 'O'
            if min_heap[0] > restore_num:
                heapq.heappush(max_heap, -restore_num)
            else:
                heapq.heappush(min_heap, restore_num)

    return ''.join(table)


# print(solution(8,2,["D 5","C","C","U 1","C"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
# print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
