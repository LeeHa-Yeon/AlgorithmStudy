def solution(n):
    standard = bin(n)[2:]
    next_num = n+1
    compare = bin(next_num)[2:]

    while standard.count('1') != compare.count('1') :
        next_num+=1
        compare = bin(next_num)[2:]

    return next_num

print(solution(78))
print(solution(15))