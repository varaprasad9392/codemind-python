def count(n):
    c=0
    while n:
        n=n//10
        c+=1
    return c    

n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if count(i)%2==0:
        c+=1
print(c)