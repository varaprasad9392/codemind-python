s=input()
u="R"
v="L"
c=d=z=0
for i in s:
    if i in u:
        c+=1
    elif i in v:
        d+=1
    if c==d:
        z+=1
print(z)