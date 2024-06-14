def fib(n):
    if n==0 or n==1:
        return 1
    return fib(n-1)+fib(n-2)
def printFN(m,n):
    l=[]
    for i in range(n+1):
        p=fib(i)
        if p>=m and p<=n:
            l.append(p)
        elif p>n:
            break
    if l==[]:
        print("No Fibonacci number")
    else:
        print(*l)
m,n=map(int,input().split())
printFN(m,n)
