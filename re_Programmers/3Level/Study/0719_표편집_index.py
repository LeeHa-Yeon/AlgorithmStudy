def solution(n, k, cmd):
    table = [ i for i in range(n)]
    ox_table = ["O"]* n
    location = table[k]
    deleted_stack = []
    for i in cmd :
        idx = table.index(location)

        if "D" in i :
            move = int(i.split()[1])
            location = table[idx+move]
        elif "U" in i :
            move = int(i.split()[1])
            location = table[idx-move]
        elif "C" in i :
            if location == table[-1] :
                location = table[-2]
                idx = table.index(location)
                deleted_stack.append(table.pop(idx+ 1))
            else :
                location = table[idx+1]
                idx = table.index(location)
                deleted_stack.append(table.pop(idx-1))
        elif "Z" in i :
            table.append(deleted_stack.pop())
            table.sort()

    for i in deleted_stack :
        ox_table[i] = "X"

    return "".join(ox_table)

# print(solution(8,2,["D 5","C","C","U 1","C"]))
print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
# print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))