n=input()
n=n.split()
for i in range(len(n)):
    if i%2==0:
        m=n[i]
        k=m[::-1]
        print(k,end=" ")
    else:
        print(n[i],end=" ")
        
    
    