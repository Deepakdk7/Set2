ax=input()
c=0
for i in range(0,len(ax)):
    for j in range(i+1,len(ax)):
        if(ax[i]==ax[j]):
            c=c+1
if c==0:
    print("Yes")
else:
    print("No")
