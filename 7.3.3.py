f=open('freedom.txt','r')
w=open('dic.txt','w')
t=f.read()

for k in set([i for i in t if i.isalnum()==False]):
    t=t.replace(k,' ')
t=t.lower().split()

r=dict()

for i in t:
    r[i]=r.get(i,0)+1

wt=''
'''print(r)'''
for i in r.keys():
    wt=wt+i+':'+str(r[i])+'\n'

w.write(wt)

f.close()
w.close()
