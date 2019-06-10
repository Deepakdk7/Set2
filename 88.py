ax=list(map(int,input().split()))
if ax[0]>ax[1]:
    y=ax[0]
else:
    y=ax[1]
while(True):
    if y%ax[0]==0 and y%ax[1]==0:
        print(y)
        break
    else:
        y=y+1
