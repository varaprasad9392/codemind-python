n=int(input())
res=su=0
for i in range(n):
    arr=list(map(int,input().split()))
    for j in range(n):
        if(i==j):
            res+=arr[j]
    for j in range(n):
        if i==n-j-1:
            su+=arr[j]
print("Principal Diagonal:",end="")
print(res)
print("Secondary Diagonal:",end="")
print(su)
