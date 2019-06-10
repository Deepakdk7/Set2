ax=input().split()
a1=int(ax[0])
a2=int(ax[1])
a=[];b=[];c=[]
for i in range(1,a1+1):
    if a1%i==0:
        a.append(i)
    if a2%i==0:
        b.append(i)
for i in a:
    for j in b:
        if i==j:
            c.append(i)
print(max(c))
