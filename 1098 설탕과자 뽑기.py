a = input()
b = a.split()
h = int(b[0])
w = int(b[1])
arr = [[0]*w for i in range(h)]

n = input()
for i in range(int(n)):
    temp = input()
    temp1 = temp.split()
    l = int(temp1[0])
    d = int(temp1[1])
    x = int(temp1[2])-1
    y = int(temp1[3])-1

    for j in range(l):
        if(d == 0):
            arr[x][y] = 1
            y += 1
        elif(d == 1):
            arr[x][y] = 1
            x += 1
        

for i in range(h):
    for j in range(w):
        print(arr[i][j], end=' ')
    print()
