t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    mid=n//2
    if(n%2==0):
        for i in range(n//2):
            if(i<mid-1):
                print(a[n-1-i],a[i],end=" ")
            else:
                print(a[n-1-i],a[i],end="")
    else:
        for i in range(n//2):
            print(a[n-1-i],a[i],end=" ")
        print(a[mid],end="")
    print()