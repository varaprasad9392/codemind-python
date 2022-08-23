import math
def isPerfectSquare(x):
    if(x >= 0):
        sr = int(math.sqrt(x))
        return ((sr*sr) == x)
    return false
n=int(input())
arr=list(map(int,input().split()))
s=0
for i in range(n):
    x=arr[i]
    if isPerfectSquare(x):
            s+=x
print(s)
        