'''
arr	result
[[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]	[4,9]
[[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]	[10,15]

'''

import numpy as np
def solution(arr) :
    def funtion(sub_arr) :
        # 모든 요소가 0이나 1일 경우
        if np.all(sub_arr==0) : return np.array([1,0])
        if np.all(sub_arr==1) : return np.array([0,1])
        n = sub_arr.shape[0]//2
        return funtion(sub_arr[:n,:n])+funtion(sub_arr[n:,:n])+funtion(sub_arr[:n,n:])+funtion(sub_arr[n:,n:])

    return funtion(np.array(arr)).tolist()

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))