a=int(input('输入数字：'))
p=input('输入运算符：')
b=int(input('输入数字：'))
if p=='+':
    result=a+b
elif p=='-':
    result=a-b
elif p=='*':
    result=a*b
elif p=='/':
    result=a/b
print('{:.2f}'.format(result))
