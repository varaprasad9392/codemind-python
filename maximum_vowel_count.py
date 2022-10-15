a=input()
a=a.split()
count=0
maxi=0
for i in range(len(a)):
    count=0
    x=str(a[i])
    for i in range(len(x)):
        if x[i] in 'aeiou':
            count+=1
    if count>maxi:
        maxi=count
print(maxi)