n=int(input())
arr=list(map(int,input().split()))
for i in range(len(arr)):
    c=z=0
    for j in range(i+1,len(arr)):
        if arr[j]>arr[i]:
            print(c+1,end=" ")
            z=1
            break
        else:
            c+=1
    if(z==0):
        print(0,end=" ")