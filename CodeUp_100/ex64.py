def miuPlus(n) :
    if n > 0 :
        return "plus"
    else :
        return "minus"

n1 = int(input())

if n1 % 2 == 0 :
    print(miuPlus(n1))
    print("even")

else :
    print(miuPlus(n1))
    print("odd")
