def rev(n):
    v=n
    r=0
    while n!=0:
        g=n%10
        r=r*10+g
        n=n//10
    return r
def change(c):
    a=[]
    p=j=0
    k=c
    while c>0:
        j=c%10
        a.append(j)
        c=c//10
    for i in range(len(a)):
        if a[i]==6:
            a[i]=9
            break
    z=b=0
    for i in range(len(a)):
       b=b*10+a[i]
    return b
n=int(input())
c=0
c=rev(n)
d=0
d=change(c)
print                                  (d)