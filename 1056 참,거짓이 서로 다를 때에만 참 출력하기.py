a = input()
b = a.split()
n1 = int(b[0])
n2 = int(b[1])

c = int((n1==1 & n2==0) | (n1==0 & n2==1))
print(c)
