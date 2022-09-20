a=int(input())
l=list(map(int,input().split()))
count=0
su=0
l1=set(l)
l2=list(l1)
for i in range(len(l2)):
    count=0
    for j in range(len(l)):
        if l2[i]==l[j]:
            count+=1
    if count==l2[i]:
        su+=1
print(su)