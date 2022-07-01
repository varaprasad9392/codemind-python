a=int(input())
s=0
for i in range(0,int(2**0.5)+1):
    for j in range(0,a+1):
        if i*i+j*j==a:
            s+=1
            break
if s==1:
    print(True)
else:
    print(False)