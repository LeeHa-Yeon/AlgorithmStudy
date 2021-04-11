'''
삽입정렬

1. 삽입 정렬은 모든 요소를 앞에서부터 차례대로 이미 정렬된 배열 부분과 비교하여,
   자신의 위치를 찾아 삽입함으로써 정렬을 완성하는 알고리즘이다.
2. 2번째 요소부터 앞에 요소들과 비교하여 본인의 자리를 찾아간다.

'''

def insertSort(v) :
    for i in range(1,len(v)) :
        j = i-1
        while(j>=0 and v[i]<v[j]) :
            j-=1
        v.insert((j+1),v[i])
        del v[i+1]
    return v


print(insertSort([7,6,1,8,5,3,9,2,4]))
