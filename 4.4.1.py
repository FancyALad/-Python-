print(r'(a)')
for i in range(1,6):
    print('*'*i)
print(r'(b)')
for i in range(1,10,2):
    print('{:^11}'.format('*'*i if i!=9 else '*'*10))
print(r'(c)')
for i in range(1,5,2):
    print('{:^5}'.format('*'*i))
for i in range(5,0,-2):
    print('{:^5}'.format('*'*i))
