a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
x=[]
for i in range(len(l1)):
    count=0
    for j in range(len(l1)):
        if l1[i]==l1[j]:
            count+=1
    if count==1 and l1[i] not in l2:
        x.append(l1[i])
count=0
for i in range(len(l2)):
    count=0
    for j in range(len(l2)):
        if l2[i]==l2[j]:
            count+=1
    if count==1 and l2[i] not in l1:
        x.append(l2[i])
print(*x)