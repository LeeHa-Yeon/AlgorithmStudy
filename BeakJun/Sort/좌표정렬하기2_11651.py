import sys

N = int(sys.stdin.readline())
coordinate = []

for _ in range(N) :
    x,y = map(int,sys.stdin.readline().split(" "))
    coordinate.append((x,y))

coordinate.sort(key=lambda x:(x[1],x[0]))

for x1,y1 in coordinate :
    print(x1,y1)