from itertools import permutations
def solution(n,m,k) :
    arr = "("*n+")"*m
    arr = set(map("".join,permutations(arr,n+m)))
    arr= list(sorted(arr))
    return arr[k-1]

print(solution(2,2,5))  # )()(
print(solution(3,4,20))  # )()(())
print(solution(4,5,1))  # (((()))))
