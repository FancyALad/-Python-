f=open('example.txt','r')
wr=open('result.txt','w')
t=f.readlines()

wt=''
for j in t:
    s=''.join([i.upper() if ord(i)>=97 and ord(i)<=122 else i.lower() for i in j])
    wt=wt+s

wr.write(wt)

f.close()
wr.close()
