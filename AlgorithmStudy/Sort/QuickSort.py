

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # pivot 첫번째원소 / tail 피벗을 제외한 리스트
    pivot = arr[0]
    tail = arr[1:]

    # 각각 분할된 왼쪽 부분 / 분할된 오른쪽 부분
    left_side = [x for x in tail if x <= pivot ]
    right_side = [x for x in tail if x > pivot ]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort([14, 7, 3, 12, 9, 11, 6, 2]))


'''
14 
7 3 12 9 11 6 2   []

7
3 6 2     12 9 11

3         12
2   6     9 11   []

 
'''