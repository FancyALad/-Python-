import math
def funcos(eps,x):
    sum=p=1
    cnt=0
    while True:
        cnt+=1
        p=x**(2*cnt)/math.factorial(2*cnt)
        if cnt%2==1:
            sum-=p
        else:
            sum+=p
        if p<eps:
            break
    return round(sum,4)
eps,x=map(float,input().split())
print(funcos(eps,x))
