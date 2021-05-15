'''
arr	return
10	true
12	true
11	false
13	false
'''

def solution(x):
    hap = sum(list(map(int,str(x))))
    if x%hap == 0 :
        return True
    return False

print(solution(12))