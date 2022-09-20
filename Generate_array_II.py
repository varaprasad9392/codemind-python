a=int(input())
b=list(map(int,input().split()))
for i in range(0,a,2):
    count=0
    while count<b[i+1]:
        print(b[i],end=' ')
        count+=1