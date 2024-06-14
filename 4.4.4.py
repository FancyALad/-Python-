a=100;b=1000;
p=[]
sum=0
for i in range(2,b+1):
    isprime=True
    for k in p:
        if i%k==0:
            isprime=False
            break

    if(isprime):
        p.append(i)
        if(i>=a):
            sum+=i
print(sum)
