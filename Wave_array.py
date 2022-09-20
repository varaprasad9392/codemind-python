a=int(input())
b=list(map(int,input().split()))
count=0
for i in range(1,a-1):
    if (b[i]>b[i-1] and b[i]<b[i+1]) or (b[i]<b[i-1] and b[i]<b[i+1]):
        count+=1
if count==(a//2)-1:
    print('yes')
else:
    print('no')
    