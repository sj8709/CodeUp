a = input()
b = a.split()
n1 = int(b[0])
n2 = int(b[1])

for i in range(1,n1+1):
    for j in range(1,n2+1):
        print('{0} {1}'.format(i, j))
