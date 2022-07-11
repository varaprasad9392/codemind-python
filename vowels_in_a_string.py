n=input()
k=input()
m=0
for i in range(len(n)):
    if n[i]==k:
        m=i
        break
if m==0:
    print("False")
else:
    print("True")
    print(m)
