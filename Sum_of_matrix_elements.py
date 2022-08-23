m=int(input())
n=int(input())
s=0
for i in range(m):
        arr=list(map(int,input().split()))
        k=0
        while(k<n):
            s+=arr[k]
            k+=1
print(s)
