import sys

N = int(sys.stdin.readline())
l = [0]*10001

for _ in range(N) :
    num = int(sys.stdin.readline())
    l[num]+=1

for i in range(1,10001) :
    if l[i]!=0 :
        for _ in range(l[i]) :
            print(i)