def math(ex) :
    stack = []

    for i in range(len(ex)) :
        if ex[i] == '(':
            stack.append(i)

        elif ex[i] == ')':
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) != 0:
        return False

    return True

ex = list("3+5")
print(math(ex))