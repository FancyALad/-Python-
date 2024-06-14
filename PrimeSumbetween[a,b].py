a,b=map(int,input().split())
if a==1:
    a=2
prime=[]
sum=0
for x in range(2,b+1):
    isprime=True
    for k in prime:
        if x%k==0:
            isprime=False
            break
    if isprime:
        if x>=a:
            sum+=x
        prime.append(x)
print(sum)
