def prime(p):
    for i in range(2,p):
        if p%i==0:
            return False
    return True

def primeSum(m,n):
    sum=0
    for i in range(m,n+1):
        if prime(i):
            sum+=i
    return sum

m,n=map(int,input("请输入两个数字m,n,确保1<=m<n:").split())
print(primeSum(m,n))
