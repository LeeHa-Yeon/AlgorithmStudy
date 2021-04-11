'''
버블 정렬

- 선택 정렬과 마찬가지로 두 개의 반복문이 필요합니다.
- 내부 반복문에서는 첫번째 값부터 이전 패스에서 뒤로 보내놓은 값이 있는 위치 전까지 앞뒤 값을 계속해서 비교해나가면서
  앞의 값이 뒤의 값보다 클 경우 자리 교대(swap)를 합니다.
- 외부 반복문에서는 뒤에서 부터 앞으로 정렬 범위를 n-1부터 1까지 줄여나갑니다.

'''

def bubble_sort(arr) :
    for i in range(len(arr)-1,0,-1) :
        swap = False
        for j in range(i) :
            if arr[j] > arr[j+1] :
                arr [j],arr[j+1] = arr[j+1],arr[j]
                swap = True
        if swap == False :
            break
    return arr
print(bubble_sort([7,6,1,8,5,3,9,2,4]))


