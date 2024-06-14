def fn(a,n):
    sum=0
    for i in range(1,n+1):
        sum+=int(str(a)*i)
    return sum
print(fn(3,3))
