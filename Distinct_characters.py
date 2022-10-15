a=input()
a=a.lower()
x=set(a)
l=sorted(x)
for i in range(len(l)):
    if ord(l[i])!=32:
        print(l[i],end='')