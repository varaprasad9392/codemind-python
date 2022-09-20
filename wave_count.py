a=int(input())
b=list(map(int,input().split()))
count=0
for i in range(1,a-1):
    if (b[i]>b[i-1] and b[i]>b[i+1]):
        count+=1
if count==(a-1)//2:
    print(count)
else:
    print('-1')