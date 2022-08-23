n=int(input())
arr=list(map(int,input().split()))
ro=int(input())
x=v=0
while(ro>0):
    x=arr[0]
    arr[0]=arr[n-1]
    for i in range(1,n):
        v=arr[i]
        arr[i]=x
        x=v
    ro-=1
for i in range(n):
    print(arr[i],end=" ")