a = input()
b = a.split()
n1 = int(b[0])
n2 = int(b[1])
n3 = int(b[2])

c1 = (n1 if (n1<n2) else n2)
c2 = (n2 if (n2<n3) else n3)
print(c1 if c1<c2 else c2)


print((n1 if (n1<n2) else n2)
      if (n1 if (n1<n2) else n2) < (n2 if (n2<n3) else n3)
      else (n2 if (n2<n3) else n3))
