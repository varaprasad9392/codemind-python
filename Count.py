n=int(input())
p=list(map(int,input().split()))
c=0
d=0
for i in range(n):
    if(p[i]%2==0):
        c+=1;
    if(p[i]%2!=0):
        d+=1
print(c, d)