l=list(range(1,31))
p=[]
index=0
for i in range(10):
    #print(l)
    index=(index+8)%len(l)
    p.append(l.pop(index))
print(p)
