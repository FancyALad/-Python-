l=[1]*30
s=[]
index=0
for i in range(10):
    num=0
    while num!=9:
        if(l[index%30]):
           num+=1
        index+=1
    l[index%30-1]=0
    s.append(index%30)
print(s)
