a = input()
b = a.split()

n1 = int(b[0])
n2 = int(b[1])
n3 = int(b[2])

c = 1
while True:
    if((c%n1 == 0)&(c%n2 == 0)&(c%n3 == 0)):
        print(c)
        break
    else:
        c+=1
