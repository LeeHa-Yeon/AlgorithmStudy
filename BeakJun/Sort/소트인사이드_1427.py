import sys
n = sys.stdin.readline()
l = list(n)[:-1]
l.sort(reverse=True)

print(int("".join(l)))