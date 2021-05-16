'''
매개변수	값
n	5
arr1	[9, 20, 28, 18, 11]
arr2	[30, 1, 21, 17, 28]
출력	["#####","# # #", "### #", "# ##", "#####"]

매개변수	값
n	6
arr1	[46, 33, 33 ,22, 31, 50]
arr2	[27 ,56, 19, 14, 14, 10]
출력	["######", "### #", "## ##", " #### ", " #####", "### # "]
'''

def solution(n, arr1, arr2):
    answer = []
    for i in range(n) :
        result = int(bin(arr1[i])[2:].zfill(n))+int(bin(arr2[i])[2:].zfill(n))
        result = str(result).translate(str.maketrans('012',' ##')).rjust(n,' ')
        answer.append(result)
    return answer

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))
print(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))