ax=input()
a=len(ax)
b=a//2
ax=list(ax)
if a%2==0:
    ax[b]="*"
    ax[b-1]="*"
else:
    ax[b]="*"
for i in ax:
    print(i,end="")
