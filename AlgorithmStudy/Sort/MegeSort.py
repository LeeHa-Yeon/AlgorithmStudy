'''
병합정렬

'''

def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftList = merge_sort(list[:mid])
    rightList = merge_sort(list[mid:])
    return merge(leftList, rightList)

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)
        elif len(left) > 0:
            result.append(left[0])
            left.pop(0)
        elif len(right) > 0:
            result.append(right[0])
            right.pop(0)
    return result

print(merge_sort([14, 7, 3, 12, 9, 11, 6, 2]))