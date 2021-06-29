'''
[2,7]	[3,11]
'''

def solution(numbers):
    answer = []
    for num in numbers :
        # 짝수일 경우
        if num % 2 == 0 :
            answer.append(int(bin(num)[2:-1]+"1",2))
        else :
            numBinary = bin(num)[2:]
            if numBinary.count("1") == len(numBinary) :
                numBinary = "10"+numBinary[1:]
                answer.append(int(numBinary,2))
            else :
                findIdx = numBinary.rfind("01")
                numBinary = numBinary[:findIdx]+"10"+numBinary[findIdx+2:]
                answer.append(int(numBinary,2))
    return answer

print(solution([2,7,21]))
print(solution([1001,337,0,1,333,673,343,221,898,997,121,1015,665,779,891,421,222,256,512,128,100]))

'''
def solution(numbers):
    for num in numbers :
        print(num)
        numBinary = bin(num)[2:].zfill(len(bin(num)[2:])+3)
        for i in range(num+1,num**2) :
            iBinary = bin(i)[2:].zfill(len(numBinary))
            print(numBinary)
            print(iBinary)
            print(bin(int(numBinary)^int(iBinary))[:])


        print("-----")
    return ""

print(solution([2,7]))
'''