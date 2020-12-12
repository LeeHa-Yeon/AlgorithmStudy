# 문제70 : 행렬 곱하기
# 행렬 2개가 주어졌을 때 곱할 수 있는 행렬인지 확인하고 곱할 수 있다면 그 결과를, 곱할 수 없다면 -1을 출력하는 프로그램을 만들어주세요.
#
# 입력
# a = ([1,2],
#      [2,4])
# b = ([1,0],
#      [0,3])

# 출력 : ([1,6],[2,12])

import numpy as np

a = ([1,2],
     [2,4])
b = ([1,0],
     [0,3])

processionA = np.array(a)
processionB = np.array(b)

print(processionA.dot(processionB))


'''
설치법 : pip install numpy
사용법 : velog 확인하기  
'''