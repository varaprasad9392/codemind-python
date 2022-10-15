n=int(input())
i=z=x=d1=d=0
for i in range(n):
    x=pow(2,i)
    if x==n:
        d=0
        break
    elif(x>n):
        d=x-n
        d1=n-(x//2)
        break
if d<=d1:
    print(d)
else:
    print(d1)