'''
citations	return
[3, 0, 6, 1, 5]	3
'''

def solution(citations):
    citations.sort( reverse=True)
    h = 0
    while h < len(citations) and citations[h]>h :
        h+=1
    return h

print(solution([22,42]))