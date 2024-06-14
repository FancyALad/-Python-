class Stock:
    def __init__(self,symbol,name,prePrice,curPrice):
        self.symbol=symbol
        self.name=name
        self.prePrice=prePrice
        self.curPrice=curPrice
    def getsymbol(self):
        return self.symbol
    def getname(self):
        return self.name
    def getprePrice(self):
        return self.prePrice
    def setprePrice(self,prePrice):
        self.prePrice=prePrice
    def getcurPrice(self):
        return self.curPrice
    def setcurPrice(self,curPrice):
        self.curPrice=curPrice
    def getChangePercent(self):
        return self.curPrice/self.prePrice

A=Stock(10001,"平头哥芯片",62.82,70.32)
print("股票名："+A.getname()+"，前一天收盘价："+str(A.getprePrice())+"，当前价："+str(A.getcurPrice())+"，当前的涨幅："+str(A.getChangePercent()))
