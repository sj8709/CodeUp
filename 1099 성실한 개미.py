arr = [[0]*10  for i in range(10)]
for i in range(10):
    a = input()
    b = a.split()
    for j in range(10):
        arr[i][j] = b[j]

x = 1
y = 1
#arr[x][y+1] 오른쪽
#arr[x+1][y] 밑

while(1):
    arr[x][y] = '9'
    if(arr[x][y+1] == '0'):
        arr[x][y+1] = '9'
        y += 1
    elif(arr[x][y+1] == '1'):
        if(arr[x+1][y] == '0'):
            arr[x+1][y] = '9'
            x += 1
        elif(arr[x+1][y] == '2'):
            arr[x+1][y] = '9'
            break
        elif(arr[x+1][y] == '1'):
            break
    elif(arr[x][y+1] == '2'):
        arr[x][y+1] = '9'
        break
    elif(arr[x+1][y] == '2'):
        arr[x][y+1] = '9'
        break
    if(x>=9 or y>=9):
        break

for i in range(10):
    for j in range(10):
        print(arr[i][j], end = ' ')
    print()
