def prime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    return 1
t=int(input())
for i in range(t):
    n=int(input())
    if(prime(n)==1):
        print(n)
    else:
        lf=sf=0
        for i in range(n+1,1000000):
            if(prime(i)==1):
                lf=i-n
                res=i
                break
        for j in range(n-1,1,-1):
            if(prime(j)==1):
                sf=n-j
                val=j
                break
        if lf>sf:
            print(val)
        elif lf==sf:
            if res<val:
                print(res)
            else:
                print(val)
        else:
            print(res)