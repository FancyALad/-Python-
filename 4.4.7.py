m,n=map(int,input('输入行数和列数（空格隔开）：').split())
matrix=[]
for i in range(m):
    matrix.append([i for i in map(int,input().split())])
for i in range(m):
    print(sum(matrix[i]))
