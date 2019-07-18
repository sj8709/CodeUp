pan = []
for i in range(19):
    a = input()
    temp = a.split()
    temp2 = []
    for j in range(19):
        temp2.append(temp[j])
    pan.append(temp2)

num = input()
for i in range(int(num)):
    xy = input()
    b = xy.split()
    x = int(b[0])-1
    y = int(b[1])-1
    for j in range(0,19):
        if(pan[x][j] == '0'):
            pan[x][j] = '1'
        elif(pan[x][j] == '1'):
            pan[x][j] = '0'

        if(pan[j][y] == '0'):
            pan[j][y] = '1'
        elif(pan[j][y] == '1'):
            pan[j][y] = '0'
        
        
for i in range(19):
    for j in range(19):
        print(pan[i][j], end=' ')
    print()
