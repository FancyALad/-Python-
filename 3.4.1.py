a=[i for i in map(int,input().split())]
b=sum(i for i in a)/len(a)
print(' '.join([str(i) for i in a if i>b]))
