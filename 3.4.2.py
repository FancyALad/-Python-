a=input()
b=list(int(i) for i in a[:-1])
weight=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
Z=list('10X987654321')
c=sum(b[i]*weight[i] for i in range(17))%11
print(Z[c]==a[-1])
