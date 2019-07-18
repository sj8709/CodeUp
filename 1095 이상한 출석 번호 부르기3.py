a = input()
b = input()
c = b.split()
m = 23
for i in c:
    t = int(i)
    if(m > t):
        m = t
print(m)
