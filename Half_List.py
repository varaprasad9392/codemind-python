n=int(input())
l=list(map(int,input().split()))
x=[]
y=[]
z=[]
for i in range(n//2):
    x.append(l[i])
for i in range(n//2,n):
    y.append(l[i])
for i in range(len(y)-1,-1,-1):
    z.append(y[i])
print(*(z+x))
    
    