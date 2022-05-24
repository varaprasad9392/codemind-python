n=int(input())
rev=0
m=n
while m>0:
    temp=m%10
    rev=rev*10+temp
    m=m//10
if rev==n:
    print('True')
else:
    print('False')