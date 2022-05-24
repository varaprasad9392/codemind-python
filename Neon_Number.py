n=int(input())
sum=0
m=n*n
while m>0:
    temp=m%10
    sum=sum+temp
    m=m//10
if sum==n:
    print('Neon Number')
else:
    print('Not Neon Number')