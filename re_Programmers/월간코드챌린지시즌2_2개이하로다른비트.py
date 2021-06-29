'''
[2,7]	[3,11]
'''

def solution(numbers):
    answer = []
    for num in numbers :
        # 짝수일 경우
        if num % 2 == 0 :
            answer.append(int(bin(num)[2:-1]+"1",2))
        # 홀수일 경우
        else :
            numBinary = bin(num)[2:]
            # 모든 비트가 1인 경우 앞에 있는 01을 10으로 바꿔줌
            if numBinary.count("1") == len(numBinary) :
                numBinary = "10"+numBinary[1:]
            # 모든 비트가 1이 아닌 경우엔 가장 마지막에 등장하는 01을 10으로 바꿔줌
            else :
                findIdx = numBinary.rfind("01")
                numBinary = numBinary[:findIdx]+"10"+numBinary[findIdx+2:]
            answer.append(int(numBinary,2))
    return answer

print(solution([2,7,21]))
print(solution([1001,337,0,1,333,673,343,221,898,997,121,1015,665,779,891,421,222,256,512,128,100]))
