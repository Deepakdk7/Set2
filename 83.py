ax=input()
a=ax.split('/')
b=ax.split('%')
for i in ax:
    if(i=='/'):
        print(int(a[0])//int(a[1]))
    elif(i=='%'):
        print(int(b[0]) % int(b[1]))
