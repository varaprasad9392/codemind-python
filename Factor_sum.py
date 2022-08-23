def fact(n):
    s=0
    for j in range(1,n+1):
        if n%j==0:
            s+=j
    return s
s=input()
z="1234567890"
a=[]
b=[]
w=0
for i in s:
    if i in z:
        a.append(ord(i)-48)
x=len(a)
for i in range(x):
    res=fact(a[i])
    if res in a:
        b.append(a[i])
        w+=1
if(w==0):
    print(-1)
else:
    b.sort()
    for i in range(len(b)):
        print(b[i],end=" ")