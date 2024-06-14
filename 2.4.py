a,n=input("输入两个不超过9的整数：").split()
print("s=",sum(list(int(str(a)*i) for i in range(1,int(n)+1))),sep='')
