f = [[0]*19 for i in range(19)]

a = input()
for i in range(int(a)):
    b = input()
    c = b.split()
    n1 = int(c[0])-1
    n2 = int(c[1])-1
    f[n1][n2] += 1

for j in range(19):
    for k in range(19):
        print(f[j][k], end=' ')
    print()
    
