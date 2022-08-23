s=input()
x=s.split()
n=int(input())
c=0
v=0
for i in range(n):
    l=input()
    u=l.split()
    v+=len(u)
    for j in u:
        if j in x:
            c+=1
if c==v:
    print(True)
else:
    print(False)