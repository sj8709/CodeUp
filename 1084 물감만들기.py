a = input()
b = a.split()
n1 = int(b[0])
n2 = int(b[1])
n3 = int(b[2])

c = 0
for i in range(0,n1):
    for j in range(0, n2):
        for k in range(0, n3):
            c += 1
            print(i, j, k)
print(c)
