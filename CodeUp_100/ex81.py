h, b, c, s = map(int,input().split(' '))
memory = h*b*c*s

print("%.1f MB" %(memory/2**23))
