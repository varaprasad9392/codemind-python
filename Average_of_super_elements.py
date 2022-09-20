a=int(input())
l=list(map(int,input().split()))
x=[]
count=0
m=0
su=0
for i in range(len(l)):
    count=0
    for j in range(len(l)):
        if l[i]==l[j]:
            count+=1
    if count==l[i] and l[i] not in x:
        su+=1
        m+=l[i]
        x.append(l[i])
if su==0:
    print('-1')
else:
    print(format(sum(x)/su,".2f"))