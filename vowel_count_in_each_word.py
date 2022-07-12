n=input()
n=n.split()
c=0
for i in n:
    c=0
    for j in i:
        if j in "aeiou":
            c+=1
    print(c,end=" ")
    