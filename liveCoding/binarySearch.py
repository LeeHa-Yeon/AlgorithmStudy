# import bisect
# mylist = [1, 2, 3, 7, 9, 11, 33]
# print(bisect.bisect(mylist, 33))

def binarySearch(data,target) :
    if len(data) == 0 :
        return False
    if len(data) == 1 and data[0] != target :
        return False
    if len(data) == 1 and data[0] == target :
        return True
    mid = len(data)//2
    if target == data[mid] :
        return True
    else :
        data.sort()
        if target < data[mid] :
            return binarySearch(data[:mid],target)
        else :
            return binarySearch(data[mid:],target)