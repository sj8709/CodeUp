a = input()
for i in range(1,int(a)+1):
    if(int(i)%3 == 0):
        print('X', end=' ')
    else:
        print(i, end=' ')
