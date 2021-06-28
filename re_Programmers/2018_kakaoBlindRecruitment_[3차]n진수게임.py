
'''
n	t	m	p	result
2	4	2	1	"0111"
16	16	2	1	"02468ACE11111111"
16	16	2	2	"13579BDF01234567"
'''

def convert(num, base):
    rev_base = ''
    if num == 0:
        return '0'
    while num > 0:
        num, mod = divmod(num, base)
        if mod == 10:
            rev_base += 'A'
        elif mod == 11:
            rev_base += 'B'
        elif mod == 12:
            rev_base += 'C'
        elif mod == 13:
            rev_base += 'D'
        elif mod == 14:
            rev_base += 'E'
        elif mod == 15:
            rev_base += 'F'
        else:
            rev_base += str(mod)
    return rev_base[::-1]

def solution(n, total, people , turn):
    answer = []
    result = []
    num = 0
    while len(answer) < total*people :
        answer.extend(list(convert(num,n)))
        num+=1

    for i in range(turn-1, len(answer), people):
        result.append(answer[i])

    return "".join(result[:total])


print(solution(2,4,2,1))
print(solution(8,16,2,1))
print(solution(16,16,2,2))
