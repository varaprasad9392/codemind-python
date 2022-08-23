a,b=map(int,input().split())
arr=[]
for i in range(a):
    x=list(map(int,input().split()))
    arr.append(x)
for i in range(b):
    ma=0
    for j in range(a):
        if ma<arr[j][i]:
            ma=arr[j][i]
    print(ma)