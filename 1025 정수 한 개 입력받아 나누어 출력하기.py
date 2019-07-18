a = input()
b = list(a)
l = len(b)
num = 0
for i in b:
    num += 1
    print("["+i+str(0)*(l-num)+"]")
