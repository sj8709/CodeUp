a = input()
b = a.split()
n1 = int(b[0])
n2 = int(b[1])
n3 = int(b[2])

s = n1
for i in range(1,n3,1):
    s += n2
print(s)
