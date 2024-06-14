import math
class QE:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        self.D=0

    def getA(self):
        return self.a
    def getB(self):
        return self.b
    def getC(self):
        return self.c
    def getD(self):
        return self.b**2-4*self.a*self.c
    def getRoot1(self):
        self.D=self.b**2-4*self.a*self.c
        if (self.D)<0:
            return 0
        else:
            return (-self.b+math.sqrt(self.D))/(2*self.a)
    def getRoot2(self):
        self.D=self.b**2-4*self.a*self.c
        if (self.D)<0:
            return 0
        else:
            return (-self.b-math.sqrt(self.D))/(2*self.a)

a,b,c=map(int,input("请输入一元二次方程的a,b,c三个值，用空格隔开：").split())
A=QE(a,b,c)
D=A.getD()
print("判别式的结果为："+str(D))
if D<0:
    print("该方程无根。")
elif D==0:
    print("方程的根是：",A.getRoot1())
else:
    print("方程的根是：",A.getRoot1(),A.getRoot2())
