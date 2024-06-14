f=open('letter.txt','r')
t=f.readlines()

A=N=L=int()

'''A记录Alphabet,N记录Number'''

for i in t:
    for j in i:
        if j.isalnum():
            if ord(j)<=57:
                N+=1
            else:
                A+=1
        else:
            L+=1
print(A,N,L)


'''计算其他字符的L会把'\n'也计入'''
