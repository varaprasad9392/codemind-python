n,k=map(int,input().split())
arr=list(map(int,input().split()))
m=0
for i in range(n):
    c=0
    for j in range(i,n):
        c+=arr[j]
        if c==k:
            m+=1
print(m)