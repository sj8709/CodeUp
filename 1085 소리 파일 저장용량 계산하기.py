a = input()
b = a.split()
n1 = int(b[0])
n2 = int(b[1])
n3 = int(b[2])
n4 = int(b[3])

s = n1*n2*n3*n4
s1 = s/(2<<22)
print("{0} MB".format(round(s1,1)))
