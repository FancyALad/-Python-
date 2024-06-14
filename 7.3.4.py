f=open('water.txt','r')
t=f.readlines()

for i in t:
    s=i.split()
    print('账户'+s[0]+'的水费是：'+str(round((int(s[13])-int(s[1]))*1.05,2)))

f.close()
