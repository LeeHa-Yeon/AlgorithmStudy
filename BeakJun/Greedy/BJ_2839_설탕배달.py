n = int(input())
big = 5
small = 3
cnt = 0


while True :
    if n % big == 0 :
        cnt+=(n//big)
        print(cnt)
        break

    n-=small
    cnt+=1

    if n < 0 :
        print("-1")
        break






