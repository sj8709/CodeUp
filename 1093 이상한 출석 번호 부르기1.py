a = input()
b = input()
c = b.split()

temp = [0] * 23

for i in c:
    temp[int(i)-1] += 1

for j in range(0, 23):
    print(temp[j], end=' ')  
