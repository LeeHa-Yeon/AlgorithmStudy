# 문제51 : merge sort 병합정렬
#
# 어떤 문제를 우선 작은 문제로 쪼개고 난 후 다시 조합하여 원래의 문제를 푼다
#
# 1. 리스트의 길이는 0 또는 1이면 이미 정렬된 것으로 본다. 그렇지 않은 경우에는
# 2. 정렬되지 않은 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.
# 3. 각 부분 리스트를 재귀적으로 합병 정렬을 이용해 정렬한다.
# 4. 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다.


# 입력: 리스트 data 6,8,3,9,10,1,2,4,7,5
# 출력: 정렬된 새 리스트

def mergeSort(n,data):

    # 종료 조건: 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요 없음
    if n <= 1:
        return data

    # 그룹을 나누어 각각 병합 정렬을 호출하는 과정
    mid = n // 2 # 중간을 기준으로 두 그룹으로 나눔
    g1 = mergeSort(len(data[:mid]),data[:mid]) # 재귀 호출로 첫 번째 그룹을 정렬
    g2 = mergeSort(len(data[mid:]),data[mid:]) # 재귀 호출로 두 번째 그룹을 정렬

    print("g1 :", g1, end="\n")
    print("g2 :", g2, end="\n")

    # 두 그룹을 하나로 병합
    result = []  # 두 그룹을 합쳐 만들 최종 결과

    while g1 and g2: # 두 그룹에 모두 자료가 남아 있는 동안 반복
        if g1[0] < g2[0]: # 두 그룹의 맨 앞 자료 값을 비교
            # g1의 값이 더 작으면 그 값을 빼내어 결과로 추가
            result.append(g1.pop(0))
        else:
            # g2의 값이 더 작으면 그 값을 빼내어 결과로 추가
            result.append(g2.pop(0))
    # 아직 남아 있는 자료들을 결과에 추가
    # g1과 g2 중 이미 빈 것은 while을 바로 지나감
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    print("result :", result, end="\n")
    return result

data = [8,6,3,10,9,2,1,7,4,5]
print(mergeSort(len(data),data))