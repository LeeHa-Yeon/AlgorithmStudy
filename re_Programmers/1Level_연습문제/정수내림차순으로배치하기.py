'''
n	return
118372	873211
'''

def solution(n):
    n = list(map(int, list(str(n))))
    n.sort(reverse=True)
    answer = ""
    for i in n :
        answer+=str(i)
    return int("".join(answer))

print(solution(118372))