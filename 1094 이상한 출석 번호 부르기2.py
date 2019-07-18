a = input()
b = input()
c = b.split()
l = len(c)
for i in range(1, l+1):
    print(c[l-i], end=' ')
