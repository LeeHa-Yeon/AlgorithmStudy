'''
선택 정렬

선택 정렬의 아이디어는 전체 데이터중 가장 작은 값을 앞으로 보내는 것입니다.
데이터의 앞에서부터 순서대로 선택하고 선택된 데이터의 뒤에 있는 데이터들 중 가장 값이 작은 데이터와 스왑(Swap)합니다.
버블 정렬과 다르게 최솟값을 찾는 탐색 과정이 추가되었고 탐색과정을 한 사이클로 볼 수 있다.

시간 복잡도 Big(O)
선택 정렬은 탐색과정에서의 반복과 선택 위치를 증가시키는 반복, 즉 두 가지 반복을 진행합니다.
탐색과정에서 약 O(N)의 시간을 필요로 하며, 사이클이 반복하는데 약 O(N)의 시간을 필요로 합니다.
즉 전체 데이터를 정렬하는 데는 최대 O(N) * O(N) = O(N^2)의 시간 복잡도를 갖습니다.
시간 복잡도를 수식으로 나타내면 다음과 같습니다.
T(n)= (n-1) + (n-2) + ...... 2 + 1 = n(n-1)/2 = O(n^2)
'''

def selectionSort(arr):

    for i in range(1,len(arr)) :
        for j in range(i,0,-1) :
            if arr[j] < arr[j-1] :
                arr[j],arr[j-1] = arr[j-1],arr[j]
            else :
                break

    return arr

print(selectionSort([7,6,1,8,5,3,9,2,4]))
