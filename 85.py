ax=input()
for i in range(0,len(ax)):
    if i%2==0:
        print(ax[i],end="")
print(" ",end="")
for i in range(0,len(ax)):
    if i%2!=0:
        print(ax[i],end="")
