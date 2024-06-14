a=map(int,input().split())
m={i:0 for i in range(10)}
for x in a:
    m[x]=m[x]+1
for k in m.keys():
    print(k,m[k])
