x=list(i for i in map(int,input().split())if i>=0)
print(sum(i for i in x if i%2==1))
