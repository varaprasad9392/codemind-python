n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    z=0
    for i in range(b):
        if i*i%b==a:
            print(i)
            z=1
            break
    if z==0:
        print(-1)