n=input()
m=""
c=0
for i in n:
    if i not in m:
        m+=i
if m==n:
    print(True)
else:
    print(False)
    