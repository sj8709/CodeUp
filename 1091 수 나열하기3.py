a = input()
b = a.split()
n1 = int(b[0])
n2 = int(b[1])
n3 = int(b[2])
n4 = int(b[3])

temp = n1

for i in range(1, n4):
    temp *= n2
    temp += n3

print(temp)
