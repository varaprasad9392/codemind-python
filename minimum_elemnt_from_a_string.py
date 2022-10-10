a=input()
arr=list(a.split())
l=arr[len(arr)-1]
ma='z'
c=0
for i in l:
    for j in i:
        if(ord(j)<ord(ma)):
            ma=j
if ma.lower() in a:
    print(ma.lower())
else:
    print(ma)