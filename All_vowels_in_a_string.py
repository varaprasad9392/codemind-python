n=input()
m=""
for i in n:
    if i in "aeiou" and i not in m:
        m+=i
if len(m)==5:
    print(True)
else:
    print(False)