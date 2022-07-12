n=input()
m=""
for i in n:
    if i in "aeiouAEIOU":
        if i not in m:
            m+=i
if len(m)==0:
    print(-1)
else:
    print(*m)