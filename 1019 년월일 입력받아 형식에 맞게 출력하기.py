a = input()
b = a.split('.')
print("{0}.{1}.{2}".format(b[0].zfill(4),b[1].zfill(2),b[2].zfill(2)))
