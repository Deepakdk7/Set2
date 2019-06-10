import math
ax=input().split()
ax=list(map(int,ax))
a=ax[0]*ax[1]
x=int(math.sqrt(a))
if x*x==a:
    print('yes')
else:
    print('no')
