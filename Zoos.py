s=input()
g=len(s)
v=d=0
for i in range (g):
    if s[i]=='z':
        d+=1
    elif s[i]=='o':
        v+=1
if(v==2*d):
    print('Yes')
else:
    print("No")