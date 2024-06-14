def CountDigit(number,digit):
    l=list(number)
    return l.count(digit)
number=input("给出一个整数：")
digit=input("给出一个在[1,9]内的数字：")
print("number中digit出现了%d次"%CountDigit(number,digit))
