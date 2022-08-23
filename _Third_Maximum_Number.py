n=int(input())
arr=list(map(int,input().split()))
x=set(arr)
z=list(x)
z.sort()
if(len(z))==3:
    print(z[0])
elif len(z)>3:
    print(z[len(z)-3])
else:
    print(max(z))