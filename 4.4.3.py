b=10000
p=[]    #素数列表
n=[]    #因子列表
l=[]    #非素数列表
for i in range(2,b+1):
    isprime=True
    for j in p:
        if i%j==0:
            l.append(i)
            isprime=False
            break
    if(isprime):
        p.append(i)
for i in l:
    for j in range(2,i//2+1):
        if(i%j==0):
            n.append(j)
    if(sum(n)+1==i):
        print(i,end=' ')
    n.clear()
        

