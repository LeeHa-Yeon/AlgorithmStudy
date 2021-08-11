import sys
user_input = int(sys.stdin.readline())
stackArr = []

for _ in range(user_input) :
    command = sys.stdin.readline()
    if "push" in command :
        stackArr.append(int(command[5:]))
    elif "top" in command :
        if len(stackArr) == 0 :
            print(-1)
        else :
            print(int(stackArr[-1]))
    elif "size" in command :
        print(len(stackArr))
    elif "empty" in command :
        if len(stackArr) == 0:
            print(1)
        else :
            print(0)
    elif "pop" in command :
        if len(stackArr) == 0 :
            print(-1)
        else :
            p = stackArr.pop()
            print(p)

