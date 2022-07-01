n=int(input())
arr=list(map(int,input().split()))
x=[]
for i in range(n):
    if arr[i] not in x:
        x.append(arr[i])
print(*x)